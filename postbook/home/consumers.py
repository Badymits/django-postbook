import json 
from channels.generic.websocket import WebsocketConsumer

# consumers file are the views equivalent of django channels 
# but they do more than just respond to requests from the client side

# this will be responsible for receiving requests 
class NotifConsumer(WebsocketConsumer):
    
    def connect(self):
        pass

