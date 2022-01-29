from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json
from channels.db import database_sync_to_async
from .models import SecondClient
from .datamanage import DatabaseMangement


class SecondUserConsumer(AsyncJsonWebsocketConsumer, DatabaseMangement):
    async def connect(self):
        print("Webbsocket Connected...")
        await self.accept()
        self.kwargs = self.scope["url_route"]["kwargs"]
        exist = await self.exist_group(self.kwargs.get('grp_name'))
        if not exist:
            await self.create_group(self.kwargs.get('grp_name'), self.kwargs.get('client_name'))
        else:
            first_client = await self.create_and_return_first_client(self.kwargs.get('grp_name'), self.kwargs.get('client_name'))
            await self.channel_layer.group_add(self.kwargs.get('grp_name'), self.channel_name)
            await self.channel_layer.group_send(self.kwargs.get('grp_name'), {'type': 'chat.message', 'msg': {'first_client': first_client, 'second_client': self.kwargs.get('client_name')}})
        await self.channel_layer.group_add(self.kwargs.get('grp_name'), self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        print("receive...")

    async def disconnect(self, close_code):
        print("Webbsocket disconnect...")
        exist = await self.exist_group(self.kwargs.get('grp_name'))
        if not exist:
            return
        await self.delete_group(self.kwargs.get('grp_name'))

    async def chat_message(self, event):
        print(event)
        await self.send_json(event['msg'])
