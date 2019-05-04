from django.db import models

# Create your models here.
class persona(models.Model):
    # Aqui se pondra los atributos de la clase persona
    name = models.CharField(max_length =40)
    last_name = models.CharField(max_length = 40)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        #aqui devuelve los atributos
        return self.name
