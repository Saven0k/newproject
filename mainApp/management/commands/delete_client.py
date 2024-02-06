from typing import Any
from django.core.management import BaseCommand

from mainApp.models import Client
from django.core.management.base import CommandParser


class Command(BaseCommand):
    help = 'Delete Client'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('id', type=int, help='Client id to delete')
        
    def handle(self, *args, **kwargs) -> str | None:
        id = kwargs['id']
        
        client = Client.objects.filter(pk=id).first()
        
        client.delete()
        self.stdout.write(self.style.ERROR(f'Deleted author {Client}'))
        