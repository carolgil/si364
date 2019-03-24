from django.db import models

# Create your models here.
# Place, Restaurant, Activity, Bar

class Place(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=128)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=False)

    def __str__(self) :
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=128)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=False)

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name_plural = "Activities"

class Bar(models.Model):
    name = models.CharField(max_length=128)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=False)

    def __str__(self) :
        return self.name
