from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class EducationBlogPost(models.Model):
    """
    Here we'll define our EducationBlogPost model
    """

    # author is linked to a registered
    # user, via the User model in the auth app.
    author = models.ForeignKey('accounts.User', on_delete=models.PROTECT)
    author_image = models.ImageField(upload_to="images", blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)  # Record how often a post is seen
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class BlogContributor(models.Model):

    name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to="images", blank=True, null=True)
    post_count = models.IntegerField(default=0)



