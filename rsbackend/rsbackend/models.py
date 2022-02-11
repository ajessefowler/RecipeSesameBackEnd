from django.db import models
from django.contrib.auth.models import User;

class Message(models.Model):
    content = models.CharField(blank=False, null=False)

    def __str__(self):
        return self.content

class Ingredient(models.Model):
    name = models.CharField(blank=False, null=False)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(blank=False, null=False)
    imageUrl = models.URLField(blank=True, null=True)
    instructions = models.CharField(blank=False, null=False)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.PositiveIntegerField(blank=False, null=False)

class RecipeBasket(models.Model):
    user = models.ForeignKey(User)
    recipes = models.ForeignKey(Recipe)

class IngredientBasket(models.Model):
    user = models.ForeignKey(User)
    ingredients = models.ForeignKey(Ingredient)
    quantity = models.PositiveIntegerField(blank=False, null=False)

