from django.urls import path,include
from . import views
from .views import *
app_name='appointment'
urlpatterns = [
    path('',views.index,name="index"),
    path('aboutpage',views.aboutpage,name="aboutpage"),
    path('service',views.service,name="service"),
    path('price',views.price,name="price"),
    path('team',views.team,name="team"),
    path('open',views.open,name="open"),
    path('admins',views.admins,name="admins"),
    path('appointment/',views.book_appointment,name="book_appointment"),
    path('appointment/unavailable/', unavailable, name='unavailable'),
    path('appointment/success/', success, name='success'),
    path('appointment/index_value/', views.index_value, name='index_value'),
   
]
