from django.db import models

# Create your models here.


class Genere(models.Model):
    nome=models.CharField(max_length=30)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name="Genere"
        verbose_name_plural="Generi"


class Autore(models.Model):
    nome=models.CharField(max_length=50)
    cognome=models.CharField(max_length=60)
    nazione=models.CharField(max_length=20)

    def __str__(self):
        return self.nome+" "+self.cognome

    class Meta:
        verbose_name="Atore"
        verbose_name_plural="Autori"


class Libro(models.Model):
    titolo=models.CharField(max_length=50)
    isbn=models.CharField(max_length=13)
    autore=models.ForeignKey(Autore,on_delete=models.CASCADE, related_name="libri")
    genere=models.ManyToManyField(Genere)

    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name="Libro"
        verbose_name_plural="Libri"