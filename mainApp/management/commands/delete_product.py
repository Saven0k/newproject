from django.core.management import BaseCommand

from mainApp.models import Product
from django.core.management.base import CommandParser


class Command(BaseCommand):
    help = 'Delete Product'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('id', type=int, help='Product id to delete')
        
    def handle(self, *args, **kwargs) -> str | None:
        id = kwargs['id']
        
        product = Product.objects.filter(pk=id).first()
        
        product.delete()
        self.stdout.write(self.style.ERROR(f'Deleted author {Product}'))
        