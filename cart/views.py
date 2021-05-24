from django.http import response
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from .cart import Cart
from Ecommerce_Store.models import Product

def cart_summary(request):
    return render(request, 'ecommerce_store/cart/summary.html')

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_qty)
        cartqty = cart.__len__()
        response = JsonResponse({'qty':cartqty})
        return response
