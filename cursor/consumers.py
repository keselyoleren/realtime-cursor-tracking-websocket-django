from django.conf import settings
from channels.generic.websocket import AsyncJsonWebsocketConsumer, WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User
import json
from channels.consumer import AsyncConsumer
from django.template.loader import render_to_string, get_template
from channels.generic.websocket import WebsocketConsumer
import urllib.request


class cursor(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'events',
            self.channel_name
        )
        
        self.accept()

    def receive(self, text_data):
        print(text_data)
        async_to_sync(self.channel_layer.group_send)(
            'events',
            {
                'type': 'cursor',
                'data': text_data
            }
        )
        # self.send(text_data)
    
    def cursor(self, event):
        print(event)
        data = event['data']

        self.send(text_data=json.dumps({
            'data':data
        }))