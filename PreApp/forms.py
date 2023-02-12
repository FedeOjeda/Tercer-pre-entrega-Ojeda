from django import forms

class FormularioClientes(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    banco = forms.CharField()
    email = forms.EmailField()
    
class FormularioProductos(forms.Form):
    
    producto = forms.CharField()
    cantidad = forms.IntegerField()
    lugar = forms.CharField()
    
class FormularioPago(forms.Form):
    
    metodo_pago = forms.CharField()
    importe =  forms.IntegerField()
    descuento = forms.DecimalField() 
    fecha = forms.DateField()