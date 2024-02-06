from django.core.management import BaseCommand

from mainApp.models import Order
from django.core.management.base import CommandParser


class Command(BaseCommand):
    help = 'Delete Order'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('id', type=int, help='Order id to delete')
        
    def handle(self, *args, **kwargs) -> str | None:
        id = kwargs['id']
        
        order = Order.objects.filter(pk=id).first()
        
        order.delete()
        self.stdout.write(self.style.ERROR(f'Deleted author {Order}'))
        