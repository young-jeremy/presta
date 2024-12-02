from django.urls import path
from . import views

app_name = 'payments'
urlpatterns = [
    path('initiate/', views.payment_view, name='payment_view'),

]