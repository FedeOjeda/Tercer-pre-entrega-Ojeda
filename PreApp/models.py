from django.db import models


class Datos_Cliente(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    banco = models.CharField(max_length=30)
    email = models.EmailField()
    
class Datos_Producto(models.Model):
    
    producto = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    lugar = models.CharField(max_length=30)
    
class Datos_Compra(models.Model):
    
    metodo_pago = models.CharField(max_length=30)
    importe =  models.IntegerField()
    descuento = models.DecimalField(decimal_places=2,max_digits=2) 
    fecha = models.DateField()