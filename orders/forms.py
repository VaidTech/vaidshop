from django import forms 

from .models import Order, Customer, OrderProduct
from products.models import Product 
from owners.models import Owner 


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
		if user.is_owner:
			owner = Owner.objects.get(user=user)
		else:
			employee = user.employee 
			owner = employee.owner
		self.fields['products'].queryset = Product.objects.filter(shop__owner=owner)



