from . import views
from django.urls import path,include
app_name = 'bankapp'
urlpatterns = [

    path('',views.index,name='index'),
    # path('login',views.login,name='login'),
    # path('registrations',views.register,name='register'),
    # path('apply',views.apply,name='apply'),
]