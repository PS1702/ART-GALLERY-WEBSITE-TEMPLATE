from django.urls import path
from Home import views

urlpatterns = [
    path ('', views.index , name = 'Home'),
    path ('about', views.about , name = 'About'),
    path ('contact', views.contact , name = 'Contact'),
    path ('abstract', views.abstract , name = 'abstract'),
    path ('sketches', views.sketches , name = 'sketches'),
    path ('digital', views.digital , name = 'digital'),
    path ('handmade', views.handmade , name = 'handmade'),
]
