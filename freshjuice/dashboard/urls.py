from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('charts/', views.charts, name='charts'),
    path('tables/', views.tables, name='tables'),
    path('colors/', views.colors, name='colors'),
    path('borders/', views.borders, name='borders'),
    path('animations/', views.animations, name='animations'),
    path('other/', views.other, name='other'),
    path('404/', views.error_404, name='404'),
    path('blank/', views.blank, name='blank'),
    path('messages/', views.messages, name='messages'),
    path('buttons/', views.buttons, name='buttons'),
    path('cards/', views.cards, name='cards'),
    path('all_alerts/', views.all_alerts, name='all_alerts'),





]