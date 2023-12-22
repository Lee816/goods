from channels.generic.websocket import AsyncWebsocketConsumer
import json


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
