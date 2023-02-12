from django.db import models


class Datos_Cliente(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    banco = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre + ('') + self.apellido
    
class Datos_Producto(models.Model):
    
    producto = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    lugar = models.CharField(max_length=30)
    
    def __str__(self):
        return self.producto
    
class Datos_Compra(models.Model):
    
    metodo_pago = models.CharField(max_length=30)
    importe =  models.IntegerField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2) 
    fecha = models.DateField()
    
    def __str__(self):
        return self.metodo_pago + '(' + str(self.importe) + ')'