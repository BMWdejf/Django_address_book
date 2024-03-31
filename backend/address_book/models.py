from django.db import models

# Create your models here.

class Address(models.Model):
    fb_id = models.IntegerField()
    last_update = models.DateTimeField()
    kod = models.CharField()
    nazev = models.TextField()
    ic = models.IntegerField(max_length=11)
    dic = models.CharField(max_length=13)
    ulice = models.CharField()
    mesto = models.CharField()
    psc = models.CharField()

    def __str__(self):
        return self.nazev