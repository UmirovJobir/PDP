from django.db import models


class Pizza(models.Model):
    title = models.CharField(max_length=190)
    resume = models.TextField()
    cost = models.CharField(max_length=90)

    def __str__(self):
        return self.title


class Pizzas(models.Model):
    img = models.ImageField(upload_to='pizza-img')
    title = models.CharField(max_length=190)
    resume = models.TextField()
    cost = models.CharField(max_length=90)

    def __str__(self):
        return self.title


class Pizaa_About(models.Model):
    img = models.ImageField(upload_to='main-pt')
    title = models.CharField(max_length=150, blank=True, null=True)
    resume = models.TextField()
