from channels.db import database_sync_to_async
from .models import SecondClient


class DatabaseMangement:
    @database_sync_to_async
    def exist_group(self, group_name):
        group = SecondClient.objects.filter(group_name=group_name).first()
        if group:
            return True
        else:
            return False

    @database_sync_to_async
    def create_group(self, group_name, client_name):
        group = SecondClient(group_name=group_name, first_client=client_name)
        group.save()
        return

    @database_sync_to_async
    def create_and_return_first_client(self, group_name, client_name):
        group = SecondClient.objects.get(group_name=group_name)
        group.second_client = client_name
        group.save()
        return group.first_client

    @database_sync_to_async
    def delete_group(self, group_name):
        SecondClient.objects.get(group_name=group_name).delete()
