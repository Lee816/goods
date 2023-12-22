from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json

from django.shortcuts import get_object_or_404

from account.models import User
from .models import Room, Message


class ChatComsumer(AsyncWebsocketConsumer):
    # 웹소켓 연결 시 실행
    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_name = f"room_{self.room_id}"

        # join room
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        # accept
        await self.accept()

    # 웹소켓 연결 종료시 실행
    async def disconnect(self, close_code):
        # reave room
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # 메세지를 받으면 실행
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        message = text_data_json["message"]
        user_id = text_data_json["user_id"]

        await self.save_message_to_db(
            room_id=self.room_id, user_id=user_id, message=message
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
            },
        )

    async def chat_message(self, event):
        message = event["message"]

        await self.send(text_data=json.dumps({"message": message}))

    @database_sync_to_async
    def save_message_to_db(self, room_id, user_id, message):
        room = get_object_or_404(Room, id=room_id)
        sender = get_object_or_404(User, id=user_id)

        Message.objects.create(room=room, sender=sender, message=message)
