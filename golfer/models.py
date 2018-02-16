from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.
class GolferProfile(models.Model):
    golfer = models.OneToOneField('accounts.User', default='', blank=True, null=True, on_delete=models.PROTECT)
    your_name = models.CharField(max_length=255)
    your_image = models.ImageField(upload_to="images", blank=True, null=True)
    about_my_golf = models.TextField(default='', blank=True, null=True)
    biggest_golfing_achievement = models.CharField(max_length=255, null=True)
    current_handicap = models.IntegerField(default=18)
    lowest_handicap = models.IntegerField(default=18)
    your_golf_club = models.CharField(max_length=255)
    whats_in_your_bag = models.TextField(max_length=600, default='', blank=True, null=True)
    swing_video = EmbedVideoField()

    def __str__(self):
        return self.your_name
