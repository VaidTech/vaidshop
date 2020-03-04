from django import forms 

from .models import Product, Stock 
from shops.models import Shop 
from owners.models import Owner 


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product 
		fields = ('title', 'price', 'shop', 'description', 'image')

	def __init__(self, user, *args, **kwargs):
		super().__init__(*args, **kwargs)
		if user.is_owner:
			owner = Owner.objects.get(user=user)
		else:
			employee = user.employee 
			owner = employee.owner
		self.fields['shop'].queryset = Shop.objects.filter(owner=owner)


class StockForm(forms.ModelForm):
	class Meta:
		model = Stock 
		fields = ('stock_type', 'stock_quantity')







