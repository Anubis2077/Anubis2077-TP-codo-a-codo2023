
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from .views import HomeView

app_name='core.marketplace',
'core.accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    
    path('', HomeView.as_view(), name='home'),

    path('marketplace/', include('core.marketplace.urls', namespace="marketplace")),
    path('users/', include('core.accounts.urls', namespace="users")),
  

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)