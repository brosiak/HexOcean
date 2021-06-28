from django.db import models
from django.contrib.auth.models import AbstractUser
from HexOcean import settings
# Create your models here.

class Image(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


class Tier(models.Model):

    hasUrl = models.BooleanField()
    hasFetchedUrl = models.BooleanField()


class ThumbnailSize(models.Model):
    width = models.IntegerField()
    tiers = models.ManyToManyField(Tier)
    

class User(AbstractUser):
    tier_id = models.ForeignKey(
        Tier,
        on_delete=models.SET_NULL,
        null=True
    )




