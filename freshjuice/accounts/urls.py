from django.urls import path
from . import views



app_name = 'accounts'
urlpatterns = [
    path('profile/<slug:slug>/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('', views.accounts, name='accounts'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('settings/', views.settings, name='settings'),
    path('activity_log/', views.activity_log, name='activity_log'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile_view/', views.profile_view, name='profile_view'),
    path('contact_support/', views.contact_support,name='contact_support'),
    path('signup_view/', views.signup,name='signup'),
    path('password_reset/', views.password_reset,name='password_reset'),

]