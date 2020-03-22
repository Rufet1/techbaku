from django.db import models
from django.urls import reverse


class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


choices = ('1', '1'), ('3', '3'), ('12', '12')


class Plus(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.CharField(max_length=255, choices=choices)

    def __str__(self):
        return str(self.name) + str(self.price) + 'manat'

    def get_absolute_url(self):
        return reverse("sale:detail", kwargs={"id": self.id})

    class Meta:
        verbose_name_plural = "plus"


class PSN(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    image = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        return reverse("sale:psn-detail", kwargs={"id": self.id})


    class Meta:
        verbose_name_plural = 'PSN'


class Game(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("sale:gamedetail", kwargs={'id':self.id})