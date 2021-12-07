from django.urls import path
from . import views

urlpatterns = [
    path('landingpage', views.landingpage, name='landingpage'),
    path('ourstory', views.ourstory, name='ourstory'),
    path('addartifact', views.addartifact, name='addartifact'),
    path('gallery', views.gallery, name='gallery'),
]
