
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import include, re_path
from django.conf.urls.static import static
from .views import HomeView
from core.marketplace.views import *#Prueba1View
from core.changuito.views import *
from core.comentarios.views import *
from core.comentarios.forms import *
from django_comments import urls as comments_urls
from django_comments.views.comments import post_comment
from core.chat import views
from core.accounts.views import CustomPasswordChangeView



app_name='core.marketplace',
'core.accounts',
'core.changuito'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    
    path('', HomeView.as_view(), name='home'),

    path('marketplace/', include('core.marketplace.urls', namespace="marketplace")),
    path('users/', include('core.accounts.urls', namespace="users")),


    #marketplace
    path('product/<slug>/update/', UpdateProductView.as_view(template_name='userproductedit.html'), name='product_edit'),
    path('product/<slug>/', ProductDetailView.as_view(template_name='productdeatil.html'), name='product_detail'),
    path('product/<slug>/buying/', formulario_compra, name='formulario_compra'),
    path('error/', error_view, name='error'),

    #changuito
    path('changuito/', CartView.as_view(template_name='cart.html'), name='changuito'),
    path('add/', cart_add, name='add'),

    #comentarios
    path('comentar/<int:object_pk>/', post_comment, {'form_class': ComentarioFormulario}, name='comments-post-comment'),
    path('product/<slug>/comments/', CommentView, name='product_comments'),

    #chat
    path('chat/rooms', views.rooms, name='rooms'),
    path('chat/<slug:slug>/', views.room, name='room'),
    
    #accounts
    path('user_profile/', CustomPasswordChangeView.as_view(template_name='user_profile.html'), name='user_profile'), 
    
    #contrib-comments
    re_path(r'^comments/', include('django_comments.urls')),
    path('comments/', include(comments_urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)