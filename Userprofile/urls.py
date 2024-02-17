from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.register,name="register"),
     path('admin-only/', views.admin_only_view, name='admin_only'),
    path('employee-only/', views.employee_only_view, name='employee_only'),

]
