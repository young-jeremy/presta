from django.urls import path
from . import views

app_name = 'services'
urlpatterns = [
    path('', views.services, name='services_home'),
    path('small_business/', views.small_business,name='small_business'),
    path('services/', views.services_card,name='services_card'),



]