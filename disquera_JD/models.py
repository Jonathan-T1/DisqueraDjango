from django.db import models

# Create your models here.

class Disquera(models.Model):
    nitDisquera = models.CharField(max_length=25)
    nombreDisquera = models.CharField(max_length=100)
    telefonoDisquera = models.CharField(max_length=15)
    direccionDisquera = models.CharField(max_length=100)
    estadoDisquera = models.BooleanField(default=False)

class Artista(models.Model):
    iddisquerafk=models.ForeignKey(Disquera, on_delete=models.CASCADE)
    noDocumento=models.CharField(max_length=20)
    tipoDocumento=models.CharField(max_length=20)
    nombreArtista=models.CharField(max_length=50)
    apellidoArtista=models.CharField(max_length=50)
    nombreArtistico=models.CharField(max_length=50)
    fNacimArtista=models.DateField(null=True, blank=True)
    emailArtista=models.CharField(max_length=100)


