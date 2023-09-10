from . import views
from django.urls import path
app_name = 'credentials'
urlpatterns = [
    path('registrations',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('home', views.home, name='home'),
    path('apply',views.apply,name='apply'),
    path('submit',views.submit,name='submit'),
]