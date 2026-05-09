from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name
    

class Ingredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name