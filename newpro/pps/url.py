from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import checkout
from .views import add_to_cart



urlpatterns = [
    path('', views.home,name='home'),
    path('drink/', views.drink,name='drink'),
    path('lunch/', views.lunch,name='lunch'), 
    path('breakfast/', views.breakfast,name='breakfast'),
    path('juice/', views.juicee,name='juice'),
    path('cart_view/', views.cart_view,name='cart'),
    #path('order/',views.order,name='order'),
    #path('process_order',views.process_order,name='process_order'),
    #path('order_success/', views.order_success, name='order_success'),
    path('checkout/', checkout, name='checkout'),
    #path('menu/', views.menu, name='menu'),



    path('add-to-cart/', add_to_cart, name='add_to_cart'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
