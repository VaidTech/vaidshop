from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.core import serializers
from django.template.loader import render_to_string
from .forms import ShopForm 
from owners.models import Owner 
from shops.models import Shop
from core.custom.decorator.decorators import shop_creator_entry_is_author


def user_is_owner(user):
	return user.is_owner 

@login_required
@permission_required('shops.add_shop', raise_exception=True)
def shop_create_view(request):
	data=dict()
	if request.method == 'POST':
		shop_form = ShopForm(request.POST, request.FILES)
		if shop_form.is_valid():
			name = shop_form.cleaned_data.get('name')
			shop_qs = Shop.objects.filter(name__iexact=name).exists()
			if shop_qs:
				data['errors'] = {'status': 'form-invalid', 'name_error': 'Shop name is already taken! Choose another name please.'}
				return JsonResponse(data)
			else:
				shop_instance = shop_form.save(commit=False)
				user = request.user 
				if user.is_owner:
					owner = Owner.objects.get(user=user)
				else:
					employee = user.employee 
					owner = employee.owner
				shop_instance.owner = owner 
				shop_instance.creator = user 
				shop_instance.save()	
	else:
		shop_form = ShopForm()
	context = {
		'shop_form': shop_form
	}
	return render(request, 'shops/shop-create.html', context)


@login_required
@shop_creator_entry_is_author
@permission_required('shops.change_shop', raise_exception=True)
def shop_update_view(request, id):
	data = dict()
	shop_instnace = Shop.objects.get(id=id)
	if request.method == 'POST':
		shop_update_form = ShopForm(request.POST, instance=shop_instnace)
		if shop_update_form.is_valid():
			name = shop_update_form.cleaned_data['name']
			shop_qs = Shop.objects.filter(name__iexact=name).exclude(id=id).exists()
			if shop_qs:
				data['errors'] = {'status': 'form-invalid', 'name_error': 'Shop name is already taken! Choose another name please.'}
				return JsonResponse(data)
			else:
				shop_update_form.save()
	else:
		shop_update_form = ShopForm(instance=shop_instnace)
	context = {
		'shop_update_form': shop_update_form,
		'shop': shop_instnace
	}
	if request.is_ajax():
		data['html_form'] = render_to_string('shops/shop-update.html', context, request=request)
		return JsonResponse(data)
	return render(request, 'shops/shop-update.html', context)


@login_required
@permission_required('shops.view_shop', raise_exception=True)
def shop_list_view(request):
	shop_qs = None 
	try: 
		user = request.user 
		if user.is_owner:
			owner = Owner.objects.get(user=user)
		else:
			employee = user.employee 
			owner = employee.owner 
		shop_qs = owner.shops.all()
	except:
		pass 
	shop_form = ShopForm()
	context = {
		'shops': shop_qs,
		'shop_form': shop_form
	}
	return render(request, 'shops/shop-list.html', context)


@login_required
@permission_required('shops.view_shop', raise_exception=True)
def shop_detail_view(request, id):
	shop_object = Shop.objects.get(id=id) 
	top4_shop_product = shop_object.products.all()[:4]
	context = {'shop': shop_object, 'top4_shop_product': top4_shop_product}
	return render(request, 'shops/shop-detail.html', context)


@login_required
# @user_passes_test(user_is_owner)
@shop_creator_entry_is_author
@permission_required('shops.delete_shop', raise_exception=True)
def shop_delete_view(request, id):
    data = dict()
    is_delete = request.GET.get('delete')
    try:
        shop_instance = Shop.objects.get(id=id)
    except:
        data['errors'] = 'does not exists'
        return redirect("/")
    if shop_instance and is_delete:
        shop_instance.delete()
        return redirect("shops:list")
    else:
        # return reverse("employees:detail", kwargs={'id': id})
        pass
    context = {
        'shop': shop_instance
    }
    if request.is_ajax():
        data['html_form'] = render_to_string('shops/shop-delete.html', context, request=request)
        return JsonResponse(data)
    return render(request, 'shops/shop-delete.html', context)


@login_required
@permission_required('shops.view_shop', raise_exception=True)
def shop_product_list_view(request, id):
	shop_object = None
	shop_product = None
	json = None
	try:
		shop_object = Shop.objects.get(id=id)
	except: 
		pass
	if shop_object is not None:
		shop_product = shop_object.products.all()
	# 	json = serializers.serialize('json', shop_product)
	# print(json)
	context = {
		"shop_product": shop_product,
		"shop_object": shop_object
	}
	return render(request, 'products/shop-product-list.html', context)