
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from .views import HomeView
from core.marketplace.views import UpdateProductView#Prueba1View

app_name='core.marketplace',
'core.accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    
    path('', HomeView.as_view(), name='home'),

    path('marketplace/', include('core.marketplace.urls', namespace="marketplace")),
    path('users/', include('core.accounts.urls', namespace="users")),


    #marketplace
    path('product/<slug>/update/', UpdateProductView.as_view(template_name='userproductedit.html'), name='product_edit'),
    #path('product/update/', Prueba1View.as_view(template_name='product_edit.html'), name='product_edit'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)