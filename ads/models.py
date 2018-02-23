from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Ad(models.Model):
    advertiser = models.ForeignKey('accounts.User', default='', blank=True, null=True, on_delete=models.PROTECT)
    your_name = models.CharField(max_length=80, default='')
    your_location = models.CharField(max_length=150, default='')
    item_name = models.CharField(max_length=45, default='')
    published_date = models.DateTimeField(blank=True, null=True)
    product_short_description = models.TextField(default='')
    contact_email = models.CharField(max_length=80, default='')
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    views = models.IntegerField(default=0)
    item_image = models.ImageField(upload_to="images", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.item_name
