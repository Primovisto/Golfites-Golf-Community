from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
import uuid


class Equipment(models.Model):
    name = models.CharField(max_length=35, default='')
    brand = models.CharField(max_length=35, default='')
    product_short_description = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand_logo = models.ImageField(upload_to="images", blank=True, null=True)
    condition = models.CharField(max_length=35, default='')
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    @property
    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.price,
            "currency": "USD",
            "item_name": self.name,
            "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
        }

        return PayPalPaymentsForm(initial=paypal_dict)

    def __str__(self):
        return self.name
