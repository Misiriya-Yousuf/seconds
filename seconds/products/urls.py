from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.products,name = 'products'),
    path('products_details/',views.products_details,name = 'products_details'),
    
    
]
