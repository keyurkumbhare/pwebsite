from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('newsletter/',views.newsletter, name='newsletter'),
    path('privacy-policy/',views.privacy, name='privacy'),
]