import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Room, Message
from main.models import Profile


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_slug = self.scope['url_route']['kwargs']['room_slug']
        self.room_group_name = 'Chat_%s' % self.room_slug


        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name

        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        profile = data['profile']
        room = data['room']
        print('receive work')
        await self.save_message(profile, room, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'profile': profile,
                'message': message,
                'room': room,
            }

        )

    async def chat_message(self, event):
        message = event['message']
        profile = event['profile']
        room = event['room']
        print('chat_message work')

        await self.send(text_data=json.dumps({
            'message': message,
            'profile': profile,
            'room': room
        }))

    @sync_to_async
    def save_message(self, profile, room, message):
        profile = Profile.objects.get(slug=profile)
        room = Room.objects.get(slug=room)
        Message.objects.create(profile=profile, room=room, content=message)
