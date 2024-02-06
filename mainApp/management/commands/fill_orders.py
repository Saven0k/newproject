from typing import Any
from django.core.management import BaseCommand
from django.core.management.base import CommandParser

from mainApp.models import Order, Client, Product
import datetime

class Command(BaseCommand):
    Order.objects.all().delete()
    help = 'Fill goods'
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        clients = Client.objects.all()
        products = Product.objects.all()
        for i in range(min(len(clients), len(products))):
            order = Order (
                client = clients[i],
                product = products[i],
                date_of_create = datetime.date(2024, 1, 30-i),
                total_cost = i ** 2,
            )        
            self.stdout.write(self.style.SUCCESS(f'Order {order} created successfully'))
            order.save()