import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required, permission_required
from core.custom.decorator.decorators import order_creator_entry_is_author
from django.http import HttpResponse
from django.forms.models import formset_factory
from .forms import CustomerForm, OrderForm
from .models import Order, OrderProduct
from products.models import Product
from owners.models import Owner


@login_required
@permission_required('orders.add_order', raise_exception=True)
def order_confirm_view(request):
	data = dict()
	if request.method == 'POST':
		customer_form = CustomerForm(request.POST)
		order_form = OrderForm(request.user, request.POST)
		if customer_form.is_valid() and order_form.is_valid():
			customer_instance = customer_form.save()
			user = request.user
			if user.is_owner:
				owner = Owner.objects.get(user=user)
			else:
				employee = user.employee 
				owner = employee.owner 
			order_obj, created = Order.objects.get_or_create(owner=owner, creator=user, active=True)
			order_obj.customer = customer_instance
			order_obj.save()
			data['order_id'] = order_obj.id
	else:
		customer_form = CustomerForm()
		order_form = OrderForm(request.user)
	context = {
		'customer_form': customer_form,
		'order_form': order_form
	}
	if request.is_ajax():
		return JsonResponse(data)
	return render(request, 'orders/order-create-update.html', context)


@login_required
@permission_required('orders.add_order', raise_exception=True)
def order_product_view(request, id):
	data = dict()
	order_obj = get_object_or_404(Order, id=id)
	order_product_qs = order_obj.products.all()
	product_id_quantity = json.loads(request.POST['product_id_quantity'])
	for product_id, quantity in product_id_quantity:
		product_id = int(product_id)
		product_obj = Product.objects.get(id=product_id)
		if product_obj not in order_product_qs:
			order_obj.products.add(product_obj, through_defaults={'quantity': int(quantity)})
			data['is_success'] = True
	order_obj.active = False 
	order_obj.save()
	if request.is_ajax():
		return JsonResponse(data)


@login_required
@permission_required('orders.change_order', raise_exception=True)
@order_creator_entry_is_author
def order_confirm_update_view(request, id):
	data = dict()
	order_object = Order.objects.get(id=id)
	if request.method == 'POST':
		customer_form = CustomerForm(request.POST, instance=order_object.customer)
		order_form = OrderForm(request.user, request.POST)
		if customer_form.is_valid() and order_form.is_valid():
			customer_name = request.POST.get('name')
			customer_phone_number = request.POST.get('phone_number')
			customer_address = request.POST.get('address')
			order_object.customer.name = customer_name
			order_object.customer.phone_number = customer_phone_number
			order_object.customer.address = customer_address
			order_object.customer.save()
			data['order_id'] = order_object.id
			data['is_update'] = True
	else:
		customer_form = CustomerForm(instance=order_object.customer)
		order_form = OrderForm(request.user, instance=order_object)
	context = {
		'customer_form': customer_form,
		'order_form': order_form,
		'order_obj': order_object
	}
	if request.is_ajax():
		return JsonResponse(data)
	return render(request, 'orders/order-create-update.html', context)


@login_required
@order_creator_entry_is_author
@permission_required('orders.change_order', raise_exception=True)
def order_product_update_view(request, id):
	data = dict()
	order_obj = get_object_or_404(Order, id=id)
	order_product_qs = order_obj.products.all()
	product_id_quantity = json.loads(request.POST['product_id_quantity'])
	existing_selected_product_list = []
	for product_id in product_id_quantity:
		existing_selected_product_list += [int(product_id[0])]
	existing_not_selected_product_list = order_product_qs.exclude(id__in=existing_selected_product_list)
	if existing_not_selected_product_list.exists():
		for existing_not_selected_product in existing_not_selected_product_list:
			order_product = OrderProduct.objects.get(product=existing_not_selected_product, order=order_obj)
			order_product.delete()
	for product_id, quantity in product_id_quantity:
		product_id = int(product_id)
		product_obj = Product.objects.get(id=product_id)
		if product_obj in order_product_qs:
			order_product = OrderProduct.objects.get(product__id=product_id, order__id=order_obj.id)
			order_product.quantity = int(quantity)
			order_product.save()
			existing_selected_product_list += [product_obj.id]
		else: 
			order_obj.products.add(product_obj, through_defaults={'quantity': int(quantity)})
	order_obj.active = False 
	order_obj.save()
	data['is_success'] = True
	data['is_update'] = True
	if request.is_ajax():
		return JsonResponse(data)


@login_required
@permission_required('orders.view_order', raise_exception=True)
def order_list_view(request):
	user = request.user 
	if user.is_owner:
		owner = Owner.objects.get(user=user)
	else:
		employee = user.employee 
		owner = employee.owner
	order_qs = Order.objects.all()
	order_qs = order_qs.filter(owner=owner)
	context = {
		'order_qs': order_qs
	}
	return render(request, 'orders/order-list.html', context)


@login_required
@order_creator_entry_is_author
@permission_required('orders.delete_order', raise_exception=True)
def order_delete_view(request, id):
	data = dict()
	is_delete = request.GET.get('delete')
	try:
		order_instance = Order.objects.get(id=id)
	except:
		data['errors'] = 'does not exists'
	if order_instance and is_delete:
		order_instance.delete()
		return redirect("orders:list")
	else:
		pass
	context = {
		'object': order_instance
	}
	if request.is_ajax():
	    data['html_form'] = render_to_string('orders/order-delete.html', context, request=request)
	    return JsonResponse(data)
	return render(request, 'orders/order-delete.html', context)