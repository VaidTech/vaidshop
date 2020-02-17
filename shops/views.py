from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .forms import ShopForm 
from owners.models import Owner 
from shops.models import Shop


@login_required()
def shop_create_view(request):
	data=dict()
	if request.method == 'POST':
		shop_form = ShopForm(request.POST, request.FILES)
		if shop_form.is_valid():
			name = shop_form.cleaned_data.get('name')
			shop_qs = Shop.objects.filter(name__iexact=name).exists()
			print(shop_qs)
			print(name)
			if shop_qs:
				data['errors'] = {'status': 'form-invalid', 'name_error': 'Shop name is already taken! Choose another name please.'}
				return JsonResponse(data)
			else:
				shop_instance = shop_form.save(commit=False)
				owner = Owner.objects.get(user=request.user)
				shop_instance.owner = owner 
				shop_instance.save()	
	else:
		shop_form = ShopForm()
	context = {
		'shop_form': shop_form
	}
	return render(request, 'shops/shop-create.html', context)

@login_required()
def shop_update_view(request, id):
	shop_instnace = Shop.objects.get(id=id)
	if request.method == 'POST':
		shop_update_form = ShopForm(request.POST, instance=shop_instnace)
		if shop_update_form.is_valid():
			name = shop_update_form.cleaned_data['name']
			shop_qs = Shop.objects.filter(name__iexact=name).exclude(id=id).exists()
			if shop_qs:
				raise ValidationError('Shop name is already exists!Please choose another name.')
			shop_update_form.save()
	else:
		shop_update_form = ShopForm(instance=shop_instnace)
	context = {
		'shop_update_form': shop_update_form,
		'shop': shop_instnace
	}
	return render(request, 'shops/shop-update.html', context)

@login_required()
def shop_list_view(request):
	owner = Owner.objects.get(user=request.user)
	shop_qs = owner.shops.all()
	shop_form = ShopForm()
	context = {
		'shops': shop_qs,
		'shop_form': shop_form
	}
	return render(request, 'shops/shop-list.html', context)

@login_required()
def shop_detail_view(request, id):
	shop_object = Shop.objects.get(id=id)
	top4_shop_product = shop_object.products.all()[:4]
	context = {'shop': shop_object, 'top4_shop_product': top4_shop_product}
	return render(request, 'shops/shop-detail.html', context)

@login_required()
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
