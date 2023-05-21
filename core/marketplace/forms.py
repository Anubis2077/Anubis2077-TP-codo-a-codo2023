from django import forms
from .models import *
from core.accounts.models import User



class ProductModelForm(forms.ModelForm):
    #metodo para agregar clases a los forms
    #name= forms.CharField(widget=forms.TextInput(attrs={'class':'clases de boostrap'})) esto lo podes copiar directamente en el models.py
    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'thumbnail',
            'slug',
            'content_url',
            'content_file',
            'active',
            'price',
            'category',
        )
       

class BuyModelForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model = Buy
        fields = (
            'email',
        )