from typing import Any
from django.core.management import BaseCommand

from mainApp.models import Product

class Command(BaseCommand):
    help = 'Fill products'
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        for i in range(1, 10):
            product = Product(
                title = f'Title {i}',
                discription = f'Description {i}',
                cost = i**2,
                amount_product = i * 2,
            )
            self.stdout.write(self.style.SUCCESS(f'Product {product} created successfully'))
            product.save()