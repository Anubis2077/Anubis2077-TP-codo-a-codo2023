from django.db import models
from django.conf import settings
import os
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.views.generic import UpdateView



User = settings.AUTH_USER_MODEL

def marketplace_directory_path(instance, filename):
    if instance.name is not None:
        thumbnail = 'media/products/{0}/{1}'.format(instance.name, filename)
        full_path = os.path.join(settings.MEDIA_ROOT, thumbnail)
        if os.path.exists(full_path):
            os.remove(full_path)
        return thumbnail
    else:
        # Manejar el caso en que instance.name es None
        # Por ejemplo, puedes generar un nombre aleatorio o utilizar un valor predeterminado
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

    price = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0), MaxValueValidator(999999.99)])
  

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