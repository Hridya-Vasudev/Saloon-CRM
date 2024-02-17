
from django.urls import path,include
from . import views

urlpatterns = [
    path('Appindex',views.Appindex,name="Appindex"),
    path('about',views.about,name="about"),
]
