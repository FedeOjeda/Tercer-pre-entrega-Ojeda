from django.urls import path

from .views import *


urlpatterns = [
    path('', inicio, name ='inicio'),
    path('/op_clientes', op_clientes, name ='op_clientes'),
    path('/op_productos', op_productos, name ='op_productos'),
    path('/op_forma_pago', op_forma_pago, name ='op_forma_pago'),
    path('/formulario_cliente', formulario_de_clientes, name ='formulario_cliente'),
    path('/formulario_producto', formulario_de_productos, name ='formulario_producto'),
    path('/formulario_pago', formulario_de_pago, name ='formulario_pago'),
    path('/busqueda_cliente', busqueda_cliente, name='busqueda_cliente'),
    path('/buscar_c', buscar_c, name='buscar_c'),
    path('/resultados_cliente', resultados_cliente, name='resultados_cliente'),
]
