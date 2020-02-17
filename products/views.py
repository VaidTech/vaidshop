from django.shortcuts import render
from django.http import JsonResponse

from .forms import ProductForm, StockForm 


def product_create_view(request):
	data = dict()
	if request.method == 'POST':
		product_form = ProductForm(request.user, request.POST, request.FILES)
		stock_form = StockForm(request.POST)
		if product_form.is_valid() and stock_form.is_valid():
			stock_instance = stock_form.save()
			product_instance = product_form.save(commit=False)
			product_instance.stock = stock_instance
			product_instance.save()
			data['is_success'] = True
	else:
		product_form = ProductForm(request.user)
		stock_form = StockForm()
	context = {
		'product_form': product_form,
		'stock_form': stock_form
	}
	if request.is_ajax():
		return JsonResponse(data)
	return render(request, 'products/product-create.html', context)











