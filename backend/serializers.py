from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Image, Thumbnail, Tier, User
from rest_flex_fields import FlexFieldsModelSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer


class ImageSerializer(FlexFieldsModelSerializer):

    # images = serializers.SerializerMethodField(method_name='get_image_sizes')
    # # images = list(images)
    # print(images)
    # # user = serializers.ModelSerializer()

    class Meta:
        model = Image
        fields = ["pk", "name", "image", "user", "expiration_time"]
        expandable_fields = {
            "image": ("backend.ImageSerializer"),
            "user": ("backend.UserSerializer")
        }

    def get_image_sizes(self, instance):
        request = self.context.get("request")
        sizes = []
        user = request.user
        tier = user.tier
        if tier.has_url:
            sizes.append(("full_size", "url"))
        thumbnails = Thumbnail.objects.filter(tiers=tier.id)
        for thumbnail in thumbnails:
            sizes.append(
                (f"thumbnail_{thumbnail.size}", f"thumbnail__{thumbnail.size}x{thumbnail.size}"))
        return VersatileImageFieldSerializer(sizes=sizes)


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
