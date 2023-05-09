from django import forms
from .models import Product
from django.core.exceptions import ValidationError


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
       