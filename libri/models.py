from django.db import models

class Libro(models.Model):
    titolo = models.CharField(max_length=200)
    autore = models.CharField(max_length=200)
    descrizione = models.TextField(blank=True)
    prezzo = models.DecimalField(max_digits=6, decimal_places=2)
    disponibile = models.BooleanField(default=True) # da cambiare in positiveintegerfield con def = 0 per numero cose
    aggiunto_il = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.titolo
# Create your models here.
