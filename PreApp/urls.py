from django.urls import path

from .views import *


urlpatterns = [
    path('', inicio, name ='inicio'),
    path('/op_clientes', op_clientes, name ='op_clientes'),
    path('/op_productos', op_productos, name ='op_productos'),
    path('/op_forma_pago', op_forma_pago, name ='op_forma_pago'),
]
