from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'PreApp/inicio.html')

def op_clientes(request):
    return render(request, 'PreApp/op_clientes.html')

def op_forma_pago(request):
    return render(request, 'PreApp/op_forma_pago.html')

def op_productos(request):
    return render(request, 'PreApp/op_productos.html')