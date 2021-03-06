from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Expert(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class SessionTypes(models.Model):

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Session(models.Model):

    Expert = models.ForeignKey('Expert', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.ForeignKey('SessionTypes', null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.IntegerField(validators=[MaxValueValidator(20)])
    length = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name.name
