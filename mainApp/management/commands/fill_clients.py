# Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой ба
from typing import Any
from django.core.management import BaseCommand
from django.core.management.base import CommandParser

from mainApp.models import Client

class Command(BaseCommand):
    help = 'Fill goods'
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        for i in range(1, 10):
            client = Client(
                name= f'Name {i}',
                email = f'Email {i}',
                number_phone = f'{i} {i +1}',
                address = f'Address {i}',
            )
            self.stdout.write(self.style.SUCCESS(f'Client {client} created successfully'))
            client.save()