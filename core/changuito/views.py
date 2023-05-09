from django.shortcuts import render
from django.views import View
from .cart import Cart
from django.shortcuts import redirect
from core.marketplace.models import Product
from django.http import JsonResponse





class CartView(View):
    template_name = 'pages/cart.html'

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        total_productos = sum(item['quantity'] for item in cart.cart.values())
        subtotals = []
        total = 0
        for item in cart.cart.values():
            subtotal = item["quantity"] * item["price"]
            subtotals.append(subtotal)
            total += subtotal
        items_and_subtotals = zip(cart.cart.values(), subtotals)
        context = {
            "cart": cart,
            "items_and_subtotals": items_and_subtotals,
            "total": total,
            "total_productos": total_productos,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            cart = Cart(request)
            product_id = request.POST.get('product_id')
            product = Product.objects.get(id=product_id)
            cart.remove(product)
            return JsonResponse({'success': True})
        return JsonResponse({'success': False})


def cart_add(request):
    cart = Cart(request)

    product_id = request.POST.get('product_id')
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    total_productos = sum(item['quantity'] for item in cart.cart.values())

    return redirect('changuito')


class CartContextMixin:
    """
    Mixin que agrega el carrito al contexto.
    """

    def get_cart(self, request):
        """
        Obtiene o crea el carrito para la solicitud dada.
        """
        return Cart(request)

    def get_context_data(self, **kwargs):
        """
        Agrega el carrito al contexto.
        """
        context = super().get_context_data(**kwargs)
        context['cart'] = self.get_cart(self.request)
        return context
