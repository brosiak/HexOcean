from django.contrib.auth.models import AnonymousUser, User
from rest_framework import serializers
from .models import Image, Thumbnail, Tier, User
from rest_flex_fields import FlexFieldsModelSerializer
from versatileimagefield.serializers import build_versatileimagefield_url_set


class ImageSerializer(FlexFieldsModelSerializer):

    images = serializers.SerializerMethodField(method_name="get_image_sizes")

    class Meta:
        model = Image
        fields = ["pk", "name", "images", "image", "user", "expiration_time"]
        expandable_fields = {
            "image": ("backend.ImageSerializer"),
            "user": ("backend.UserSerializer"),
        }

    def get_image_sizes(self, instance):
        request = self.context.get("request", None)
        sizes = []
        if request.user.is_anonymous:
            raise serializers.ValidationError("Anonymous user rejected")
        user = instance.user
        tier = user.tier
        if tier is None:
            return
        if tier.has_url:
            sizes.append(("full_size", "url"))
        thumbnails = Thumbnail.objects.filter(tiers=instance.user.tier.id)
        for thumbnail in thumbnails:
            sizes.append(
                (
                    f"thumbnail_{thumbnail.size}",
                    f"thumbnail__{thumbnail.size}x{thumbnail.size}",
                )
            )

        return build_versatileimagefield_url_set(instance.image, sizes, request=request)


class ThumbnailSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ["pk", "name", "size", "tiers"]


class TierSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Tier
        fields = ["pk", "name", "has_url", "can_fetch_url"]
        expandable_fields = {
            "thumbnails": ("backend.ThumbnailSerializer", {"many": True}),
            "users": ("backend.UserSerializer", {"many": True}),
        }


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ["pk", "username", "tier"]
