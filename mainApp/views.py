from django.shortcuts import render
import logging
from .models import Client, Product, Order
from .forms import ProductAddForm
# from django.core.files.storage import FileSystemStorage

import datetime
# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    logger.info('index get request ')
    return render(request, 'mainApp/index.html')

def about(request):
    logger.info('about get request ')
    return render(request, 'mainApp/about.html')


def goods(request, client_id, days):
    client = Client.objects.get(id=client_id)
    orders = Order.objects.filter(client=client)
    for i in orders:
        print(i.total_cost)
    context = {
        'title': 'Список покупок',
        'header': f'Список покупок за {days}',
        'goods': orders,   
    }
    
    logger.info('about get request ')
    return render(request, 'mainApp/goods.html', context=context)


def add_product(request):
    if request.method == 'POST':
        form = ProductAddForm(request.POST, request.FILES)
        message = 'Ошибка данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            discription = form.cleaned_data['discription']
            date_of_add = form.cleaned_data['date_of_add']
            cost = form.cleaned_data['cost']
            amount_product = form.cleaned_data['amount_product']
            photo = form.cleaned_data['photo']
            logger.info(f'Получили {title=}\n {discription=}\n {cost=} \n {amount_product=} \n {date_of_add}')
            product = Product(title=title, discription=discription, cost=cost, amount_product=amount_product, date_of_add=date_of_add)
            product.save()		
            message = 'Продукт сохранен'
            
    else: 
        form =  ProductAddForm()
        message = 'Заполните форму'
    
    return render(request, 'mainApp/add_product.html', {'form': form, 'message': message})