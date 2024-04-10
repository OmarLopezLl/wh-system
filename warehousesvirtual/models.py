from django.db import models

# Create your models here.
class Tipo_Negocio(models.Model):
    descripcion = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Tipo de Negocio"
        verbose_name_plural = "Tipo de Negocio"

    def __str__(self):
        return self.descripcion

class Unidad_Medida(models.Model):
    codigo_medida=models.CharField(max_length=4)
    nombre_medida=models.CharField(max_length=20)
    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidad de Medida"
    def __str__(self):
        return self.nombre_medida
    
class Pais(models.Model):
    nombre=models.CharField(max_length=40)
    numero_habitantes=models.PositiveBigIntegerField()
    extension=models.PositiveBigIntegerField()
    unidad_med =  models.ForeignKey(Unidad_Medida, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Pais"    
    def __str__(self):
        return self.nombre    

class Ciudad(models.Model):
    nombre=models.CharField(max_length=40)
    numero_habitantes=models.PositiveBigIntegerField()
    extension=models.PositiveBigIntegerField()
    unidad_med =  models.ForeignKey(Unidad_Medida, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE) 
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudad"    
    def __str__(self):
        return "{}" "{}".format(self.nombre,  self.pais.nombre)     

class Zonas(models.Model):
    zona=models.CharField(max_length=40)
    ciudad= models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    comentarios = models.TextField(blank=True)
    class Meta:
        verbose_name = "Zona"
        verbose_name_plural = "Zona"    
    def __str__(self):
        return self.zona
    
class Persona(models.Model):  
    nombre = models.CharField(max_length=30)  
    email = models.EmailField(blank=True)  
    fecha_nac = models.DateField()  
    ciudad = models.CharField(max_length=100, blank=True) 


    

    