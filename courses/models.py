from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Course(models.Model):
    """
    Here we'll define our Post model
    """

    # author is linked to a registered
    # user, via the User model in the auth app.
    name = models.CharField(max_length=200)
    course_image = models.ImageField(upload_to="images", blank=True, null=True)
    url = models.URLField(max_length=200, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
