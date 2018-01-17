from __future__ import unicode_literals
from django.db import models


class Ad(models.Model):
    advertiser = models.ForeignKey('accounts.User', default='', blank=True, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=35, default='')
    condition = models.CharField(max_length=35, default='Used')
    published_date = models.DateTimeField(blank=True, null=True)
    product_short_description = models.TextField(default='')
    location = models.CharField(max_length=150, default='')
    contact_email = models.CharField(max_length=80, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.name
