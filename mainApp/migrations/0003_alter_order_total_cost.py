# Generated by Django 4.2.1 on 2024-01-25 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_alter_product_amount_product_alter_product_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_cost',
            field=models.IntegerField(),
        ),
    ]
