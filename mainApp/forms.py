import datetime
from django import forms
from .models import Product

class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'discription', 'cost', 'amount_product', 'date_of_add', "photo"]
    
    
    # title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Введите название продукта'}))
    # discription = forms.CharField(max_length=550, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Описание продукта'}))
    # date_of_add = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control', 'type':'date'}))
    # amount_product = forms.IntegerField(min_value=1, max_value=1000)
    # cost = forms.IntegerField(min_value=1, max_value=100000)
    # photo = forms.ImageField()