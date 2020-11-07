from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Nutrients(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    Food = models.CharField(max_length=254)
    Grams = models.DecimalField(max_digits=6, decimal_places=2)
    Calories = models.IntegerField(max_digits=6)
    Protein = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    Fat = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    Sat.Fat = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    Fiber = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    Carbs = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.Food
