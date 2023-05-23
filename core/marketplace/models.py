from django.db import models
from django.conf import settings
import os
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.views.generic import UpdateView
from .choices import CATEGORY_CHOICES



User = settings.AUTH_USER_MODEL

def marketplace_directory_path(instance, filename):
    if instance.name is not None:
        thumbnail = 'media/products/{0}/{1}'.format(instance.name, filename)
        full_path = os.path.join(settings.MEDIA_ROOT, thumbnail)
        if os.path.exists(full_path):
            os.remove(full_path)
        return thumbnail
    else:
       
        pass

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=100)
    description=models.TextField()
    thumbnail = models.ImageField(upload_to=marketplace_directory_path)
    slug=models.SlugField(unique=True)
    content_url = models.URLField(blank=True, null=True)
    # content_file = models.FileField(blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    content_file = models.FileField(blank=True, null=True)
    active = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web_apps',)

    price = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0), MaxValueValidator(9999999999.99)])
  

    def __str__(self):
        return self.name
    
    def clean(self):
        if self.price < 100:
            raise ValidationError('Price must be greater than $100.')
        super().clean()



class PurchasedProduct(models.Model):
    email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    

class Buy(models.Model):
    comprador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='compras')
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ventas')
    email= models.EmailField()
    producto = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='purchases')
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(decimal_places=4, max_digits=100, null=True)
    categoria = models.CharField(max_length=100,null=True)

    #metodo_pago= models

    def __str__(self):
        return f"Compra {self.id} - {self.usuario.username} - {self.producto.nombre}"