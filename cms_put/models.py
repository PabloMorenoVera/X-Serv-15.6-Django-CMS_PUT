from django.db import models

# Create your models here.
class Page(models.Model):
    nombre = models.CharField(max_length = 128)
    pagina = models.TextField()
