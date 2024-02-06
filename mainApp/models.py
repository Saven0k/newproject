# Создайте три модели Django: клиент, товар и заказ.

# Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента

# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара

# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа

from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    number_phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    date_of_register = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=200)
    cost = models.IntegerField()
    amount_product = models.IntegerField()
    date_of_add = models.DateField()
    photo = models.ImageField(upload_to='photos/')
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_of_create = models.DateField(auto_now_add=True)
    total_cost = models.IntegerField()
    