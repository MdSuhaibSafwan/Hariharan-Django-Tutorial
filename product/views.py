from django.shortcuts import render
from product.models import Product


def index(request):
	products_qs = Product.objects.get_top_rated_product_for_index()

	context = {
		"products": products_qs, # key-value pair
	}

	return render(request, "product/index.html", context=context)

