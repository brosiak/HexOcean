from django.db import models
from django.contrib.auth.models import AbstractUser
from HexOcean import settings
from rest_framework.decorators import api_view
from versatileimagefield.fields import VersatileImageField

# Create your models here.


class ImagesManager(models.Manager):
    def images_for_user(self, user):
        if user.is_anonymous:
            return None
        return super(ImagesManager, self).get_queryset().filter(user=user)


class Image(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="images",
        related_query_name="image",
    )
    image = VersatileImageField("image", upload_to="images/")
    expiration_time = models.DurationField(blank=True, null=True)

    def __str__(self):
        return self.name

    objects = ImagesManager()


class Tier(models.Model):
    name = models.CharField(max_length=255)
    has_url = models.BooleanField()
    can_fetch_url = models.BooleanField()

    def __str__(self):
        return self.name


class Thumbnail(models.Model):
    name = models.CharField(max_length=255)
    size = models.IntegerField()
    tiers = models.ManyToManyField(
        Tier, related_name="thumbnails", related_query_name="thumbnail"
    )

    def __str__(self):
        return self.name


class User(AbstractUser):
    tier = models.ForeignKey(
        Tier,
        on_delete=models.SET_NULL,
        null=True,
        related_name="user",
        related_query_name="user",
    )

    def __str__(self):
        return self.username
