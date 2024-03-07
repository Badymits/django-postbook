import json 
from channels.generic.websocket import AsyncWebsocketConsumer

# consumers file are the views equivalent of django channels 
# but they do more than just respond to requests from the client side, they can also initiate requests.

# this will be responsible for receiving requests 
class NotifConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.group_name = 'notification'
        
        # join to group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        
        await self.accept()
        
    async def disconnect(self, code):
        # leave group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
    
    
    # receive messages from the websocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        
        if text_data_json['post_id']:
            post_id = text_data_json['post_id']
            
    
        event = {
            'type': 'send_message',
            'message': message,
            'post_id': post_id if True else None
        }

        await self.channel_layer.group_send(self.group_name, event)
    
    # receive message from group
    async def send_message(self, event):
        message = event['message']
        print('the message', message)
        
        if event['post_id'] is not None:
            post_id = event['post_id']
            print('the post', post_id)
        
        # send message to websocket
        await self.send(text_data=json.dumps({'message': message, 'post_id': post_id if True else None}))
        
        

