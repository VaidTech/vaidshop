from django import forms 

from .models import Product, Stock 
from shops.models import Shop 


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product 
		fields = ('title', 'price', 'shop', 'description', 'image')

	def __init__(self, user, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['shop'].queryset = Shop.objects.filter(owner__user__username=user)


class StockForm(forms.ModelForm):
	class Meta:
		model = Stock 
		fields = ('stock_type', 'stock_quantity')







