from django.db import models


# Create your models here.
class Golfer(models.Model):
    name = models.CharField(max_length=255)
    handicap = models.IntegerField(default=18)
    golf_club = models.CharField(max_length=255)
    your_bag = models.ImageField(upload_to="images", blank=True, null=True)
    swing = models.FileField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.name


