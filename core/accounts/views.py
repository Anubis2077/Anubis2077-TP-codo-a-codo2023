from allauth.account.views import PasswordChangeView
from allauth.account.forms import ChangePasswordForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from core.marketplace.models import Product

class CustomPasswordChangeView(PasswordChangeView):
    form_class = ChangePasswordForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.get_form()
        # Agregar los campos del formulario al contexto
        context['oldpassword_field'] = form['oldpassword']
        context['password1_field'] = form['password1']
        context['password2_field'] = form['password2']

        #productos publicados por el usuario
        products = Product.objects.filter(user=self.request.user)
        context['products'] = products

        #productos comprados por el usuario
         
        products_purchased = Product.objects.filter(purchases__usuario=self.request.user)
        context['products_purchased'] = products_purchased


        return context
    
    def form_valid(self, form):
        # Guardar la nueva contraseña y realizar acciones necesarias
        form.save()
        messages.success(self.request, "¡La contraseña se cambió exitosamente!")
        return HttpResponseRedirect(reverse("home"))
    