from django.db import models
from django.db.models.signals import pre_save, m2m_changed

from accounts.models import User 
from products.models import Product

from owners.models import Owner 


class Order(models.Model):
	owner 			= models.ForeignKey(Owner, on_delete=models.CASCADE)
	creator 		= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="orders")
	customer 		= models.ForeignKey('Customer', on_delete=models.CASCADE, blank=True, null=True, related_name="orders")
	products 		= models.ManyToManyField(Product, through='OrderProduct', related_name='orders')
	active			= models.BooleanField(default=True)
	created_at 		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user) + " Order"


class Customer(models.Model):
	name 			= models.CharField("customer name", max_length=120)
	phone_number 	= models.CharField(max_length=11)
	address			= models.CharField(max_length=200)

	def __str__(self):
		return str(self.name)


class OrderProduct(models.Model):
	order 	= models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_products")
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products_order")
	quantity = models.PositiveIntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.id)
		







