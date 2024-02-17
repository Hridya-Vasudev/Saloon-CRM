from django . urls import path
from . import views

urlpatterns = [
    path('',views.client_list,name="client_list"),
    path('add/',views.add_client,name="add_client"),
    path('<int:id>/delete/',views.client_delete,name="client_delete"),
    path('<int:id>/convert/',views.convert_customer,name='convert_customer')
]
