from django.urls import path
from .views import SellView, UserProductsListview
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name='core.marketplace'

urlpatterns = [
    
    path('sell/', SellView.as_view(template_name='sell.html'), name='sell'),
    path('product_list/', UserProductsListview.as_view(template_name='userproductlist.html'), name='product_list'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
