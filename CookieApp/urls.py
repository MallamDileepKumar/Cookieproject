from django.urls import path
from CookieApp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('display/',views.display,name='display'),
]