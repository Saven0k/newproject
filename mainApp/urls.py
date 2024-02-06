from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('goods/<int:client_id>/<int:days>', views.goods, name='goods'),
    path('add-product/', views.add_product, name='add_product'),
]
