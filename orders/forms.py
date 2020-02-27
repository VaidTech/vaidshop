from django import forms 

from .models import Order, Customer, OrderProduct
from products.models import Product 


class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ('name', 'phone_number', 'address')


class OrderForm(forms.ModelForm):
	class Meta:
		model = Order 
		fields = ('products',)

	def __init__(self, user, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['products'].queryset = Product.objects.filter(shop__owner__user=user)



