from typing import Any
from django.db import models
from django.views import View
from django.views.generic.edit import UpdateView
from .models import Product
from .forms import *
from django.core.paginator import Paginator
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
from django.views.generic import UpdateView
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.

class SellView(View):
    template_name = 'sell.html'
    product_list = 'pages/userproductlist.html'
    success_url = reverse_lazy('core.marketplace:product_list')

    def get(self, request, *args, **kwargs):
        form = ProductModelForm()
        context = {'form': form}

        return render(request,'pages/sell.html', context)

    def post(self, request, *args, **kwargs):
        product = Product.objects.filter(active=True)
        form = ProductModelForm(request.POST, request.FILES)
        
        if form.is_valid():
            

            product = form.save(commit=False)
            product.user = request.user
            #product.thumbnail = thumbnail_url  # Guardar la URL en el modelo
            product.save()
            print('el formulario se envio correctamente')
            # Imprimir los datos del formulario
            print(form.cleaned_data)
            return redirect (self.success_url)
        else:
            context = {'form': form}
            print('no se envio un carajo')
            return render(request, 'pages/sell.html', context)

    def user_product_list(self, request):
        products = Product.objects.filter(user=request.user)
        context = {'products': products}
        return render(request, context)

    
class UserProductsListview(View):
    template_name = 'pages/userproductlist.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(user__exact=self.request.user)

        

        context={
            'products': products
        }
        return render(request,'pages/userproductlist.html', context)
    
class UpdateProductView(LoginRequiredMixin, UpdateView):
    template_name="pages/userproductedit.html"
    form_class=ProductModelForm
    success_url= reverse_lazy('core.marketplace:product_list')

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)  
    

class ProductDetailView(View):
    template_name = 'pages/productdetail.html'

    def get(self, request, slug, *args, **kwargs):
        product = get_object_or_404(Product, slug=slug)
        user = request.user

        context={
            'product': product,
            'user': user,
        }

        return render(request, 'pages/productdetail.html', context)


#def comprar_producto(request, slug):
#    # Obtener el producto a comprar
#    producto = get_object_or_404(Product, slug=slug)
#    
#    return render(request, 'pages/compra_exitosa.html', {'product': producto})




@login_required
def formulario_compra(request, slug):
    producto = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = BuyModelForm(request.POST)
        print(form.errors)
        if form.is_valid():
            email = form.cleaned_data['email']
            compra = Buy(
                usuario=request.user,
                producto=producto,
                cantidad=1,
                email=email,
                precio=producto.price,
                categoria= producto.category       
            )

            
            compra.save()
            print("categoria:" + str(compra.categoria))
            print("precio:" + str(compra.precio))
            print("la compra se realizo exitosamente")

            
            return render(request, 'pages/compra_exitosa.html')
    else:
        form = BuyModelForm()
        print("la compra no se realizo ")

    
    return render(request, 'pages/formulario_compra.html', {'product': producto, 'form': form})

