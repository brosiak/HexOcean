from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Image, Thumbnail, Tier, User
from rest_flex_fields import FlexFieldsModelSerializer


class ImageSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Image
        fields = ["pk", "name", "image", "expiration_time"]
        expandable_fields = {
            "user": ("backend.UserSerializer")
        }


class ThumbnailSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ["pk", "name", "size", "tiers"]


class TierSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Tier
        fields = ["pk", "name", "has_url", "can_fetch_url"]
        expandable_fields = {
            "thumbnails": ("backend.ThumbnailSerializer", {'many': True}),
            "users": ("backend.UserSerializer", {'many': True}),
        }


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ["pk", "username", "tier"]
