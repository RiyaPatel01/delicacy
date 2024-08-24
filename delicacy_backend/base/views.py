from django.shortcuts import render
from django.http import JsonResponse
from .products import products

# Create your views here.

def getRoutes(request):
    return JsonResponse('Welcome', safe=False)

def getProducts(request):
    return JsonResponse(products, safe=False)

def getProductById(request, id):
    product = next((item for item in products if item['_id'] == id), None)
    if product:
        return JsonResponse(product, safe=False)
    else:
        return JsonResponse({'message': 'Product not found'}, status=404)
    

