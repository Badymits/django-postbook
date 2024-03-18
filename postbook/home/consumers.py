import json 
from django.shortcuts import get_object_or_404
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from accounts.models import Account
from home.models import Notification

# consumers file are the views equivalent of django channels 
# but they do more than just respond to requests from the client side, they can also initiate requests.

# groups are simply a collection of channels
# channels are basically mailboxes that represent users

# this will be responsible for receiving requests 
class NotifConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.user = self.scope['user'].username # the logged in user
        self.target_user = self.scope.get("url_route").get("kwargs").get("username") # username is unique

        self.user_room_name = f'notifications_for_{self.user}'
        
        print('the user group', self.user_room_name)
        if self.scope["user"].is_anonymous:
            # Reject the connection
            self.close()
        else:
            # join to group
            await self.channel_layer.group_add(
                self.user_room_name,
                self.channel_name, # this will be created automatically for each user
            )
            # self.groups.append(self.user_group_name) # important otherwise some cleanup does not happened on disconnect.
            await self.accept()
        
    async def disconnect(self, code):
        # leave group
        await self.channel_layer.group_discard(self.user_room_name, self.channel_name)
    
    
    # receive messages from the websocket/ the frontend
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        target_user = await database_sync_to_async(Account.objects.get)(username=self.target_user)
        
        if text_data_json['post_id']:
            post_id = text_data_json['post_id']
        event = {
            'type': 'send_notification',
            'message': message,
            'post_id': post_id if True else None
        }
        
        # create notification
        notif_obj = Notification(
            sender=self.scope['user'],
            receiver=target_user,
            message=message
        )
        
        await database_sync_to_async(notif_obj.save)()
        
        await self.channel_layer.group_send(
            f'notifications_for_{target_user.username}', 
            event
        )
        
    # sends message to intended user
    async def send_notification(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'post_id': event['post_id']
        }))
        

