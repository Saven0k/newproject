# Generated by Django 4.2.1 on 2024-01-30 14:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_alter_order_total_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_of_create',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
