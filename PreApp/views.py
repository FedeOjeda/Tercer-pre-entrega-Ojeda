from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def inicio(request):
    return render(request, 'PreApp/inicio.html')

def op_clientes(request):
    return render(request, 'PreApp/op_clientes.html')

def op_forma_pago(request):
    return render(request, 'PreApp/op_forma_pago.html')

def op_productos(request):
    return render(request, 'PreApp/op_productos.html')

def formulario_de_clientes(request):
    
    if request.method == 'POST':
        mi_formulario = FormularioClientes(request.POST)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente = Datos_Cliente(
                            nombre=informacion['nombre'],
                            apellido=informacion['apellido'],
                            banco=informacion['banco'],
                            email=informacion['email'],
                        )
            cliente.save()
            return redirect('op_clientes')

    
    mi_formulario = FormularioClientes()
    return render(request, 'PreApp/formulario_cliente.html', {'formulario_cliente': mi_formulario})

def resultados_cliente(request):
    return render(request, 'PreApp/resultados_cliente.html')

def formulario_de_productos(request):
    
    if request.method == 'POST':
        mi_formulario = FormularioProductos(request.POST)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            producto = Datos_Producto(
                            producto=informacion['producto'],
                            cantidad=informacion['cantidad'],
                            lugar=informacion['lugar'],
                        )
            producto.save()
            return redirect('op_productos')

    
    mi_formulario = FormularioProductos()
    return render(request, 'PreApp/formulario_producto.html', {'formulario_producto': mi_formulario})

def formulario_de_pago(request):
    
    if request.method == 'POST':
        mi_formulario = FormularioPago(request.POST)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            producto = Datos_Compra(
                            metodo_pago=informacion['metodo_pago'],
                            importe=informacion['importe'],
                            descuento=informacion['descuento'],
                            fecha=informacion['fecha'],
                        )
            producto.save()
            return redirect('op_forma_pago')

    
    mi_formulario = FormularioPago()
    return render(request, 'PreApp/formulario_pago.html', {'formulario_pago': mi_formulario})

def busqueda_cliente(request):
    return render(request, 'PreApp/busqueda_cliente.html')


def buscar_c(request):
    
    if request.GET['nombre']:
        mi_nombre = request.GET['nombre']
        resultado = Datos_Cliente.objects.filter(nombre__icontains=mi_nombre)
        return render(request, 'PreApp/resultados_cliente.html', {'clientes': resultado, 'nombre': mi_nombre})
    respuesta = 'No se encontro ese cliente'
    return HttpResponse(respuesta)

def resultados_cliente(request):
    return render(request, 'PreApp/resultados_cliente.html')

def busqueda_productos(request):
    return render(request, 'PreApp/busqueda_producto.html')

def buscar_p(request):
    
    if request.GET['producto']:
        mi_producto = request.GET['producto']
        resultado = Datos_Producto.objects.filter(producto__icontains=mi_producto)
        return render(request, 'PreApp/resultados_producto.html', {'objetos': resultado, 'producto': mi_producto})
    
    
    respuesta = 'No se encontro el producto'
    return HttpResponse(respuesta)

def resultados_producto(request):
    return render(request, 'PreApp/resultados_producto.html')

def busqueda_pago(request):
    return render(request, 'PreApp/busqueda_pago.html')

def buscar_fdp(request):
    
    if request.GET['forma_de_pago']:
        mi_pago = request.GET['forma_de_pago']
        resultado = Datos_Compra.objects.filter(metodo_pago__icontains=mi_pago)
        return render(request, 'PreApp/resultados_pago.html', {'pago': resultado, 'forma_de_pago': mi_pago})
    
    
    respuesta = 'No se encontro el metodo de pago'
    return HttpResponse(respuesta)

def resultados_pago(request):
    return render(request, 'PreApp/resultados_pago.html')