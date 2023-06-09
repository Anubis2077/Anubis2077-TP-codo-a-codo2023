from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from core.marketplace.models import Product
from core.marketplace.forms import ProductModelForm
from core.changuito.cart import Cart


class HomeView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(active=True)
        form = ProductModelForm()

        digital_products_data = None

        if products:
            paginator = Paginator(products, 9)
            page_number = request.GET.get('page')
            digital_products_data = paginator.get_page(page_number)

        cart = Cart(request)
        total_productos = sum(item['quantity'] for item in cart.cart.values()) # Crear instancia del carrito
        context = {
            'products': digital_products_data,
            'form': form,
            'cart': cart,
            'total_productos': total_productos, # Agregar el carrito al contexto manualmente
        }

        return render(request, 'pages/index.html', context)

    def post(self, request, *args, **kwargs):
        products = Product.objects.filter(active=True)

        form=ProductModelForm()

        if request.method == "POST":
            form=ProductModelForm(request.POST, request.FILES)

            if form.is_valid():
                form.user=request.user
                name = form.cleaned_data.get('name')
                description = form.cleaned_data.get('description')
                thumbnail = form.cleaned_data.get('thumbnail')
                slug = form.cleaned_data.get('slug')
                content_url = form.cleaned_data.get('content_url')
                content_file = form.cleaned_data.get('content_file')
                price = form.cleaned_data.get('price')
                active = form.cleaned_data.get('active')

                p, created = Product.objects.get_or_create(user=form.user,name=name,description=description, thumbnail=thumbnail, slug=slug, content_url=content_url, content_file=content_file,price=price, active=active)
                p.save()
                return redirect('home')

        digital_products_data = None

        if products:
            paginator = Paginator(products, 9)
            page_number = request.GET.get('page')
            digital_products_data = paginator.get_page(page_number)
        
        cart = Cart(request) # Crear instancia del carrito
        context={
            'products':digital_products_data,
            'cart': cart, # Agregar el carrito al contexto manualmente
            'form':form
        }
        return render(request, 'pages/index.html', context)


