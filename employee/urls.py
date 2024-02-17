from django.urls import path
from . import views
urlpatterns = [
    path('', views.view_employee, name='view_employee'),
    path('add_employee/',views.add_employee,name="add_employee"),
    path('<int:pk>/delete/',views.delete_employee,name="delete_employee"),
    path('<int:pk>/update/',views.update_employee,name="update_employee"),
    #  path('<int:pk>add_comment/',views.add_comment,name="add_comment"),
]
