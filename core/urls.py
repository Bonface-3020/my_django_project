from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/',views.about,name='About'),
    path('products/',views.products,name='Products'),
    path('services/',views.services,name='Services'),
    path('contact/',views.contact,name='Contact')
]