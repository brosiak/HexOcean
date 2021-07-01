from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import (
    ImageSerializer,
    ThumbnailSerializer,
    TierSerializer,
    UserSerializer,
)
from .models import (
    Image,
    User,
    Thumbnail,
    Tier
)
from rest_flex_fields.views import FlexFieldsModelViewSet
from rest_flex_fields import is_expanded
from django.http import HttpResponse


class ImageViewSet(FlexFieldsModelViewSet):
    serializer_class = ImageSerializer
    permit_list_expands = ["user", "image"]
    filterset_fields = ("user",)

    def get_queryset(self):
        request = self.request
        if request.user.is_anonymous:
            return None
        elif request.user.is_superuser:
            queryset = Image.objects.all()
        else:
            queryset = Image.objects.images_for_user(request.user)
        if is_expanded(self.request, "user"):
            queryset = queryset.select_related("user")

        if is_expanded(self.request, "image"):
            queryset = queryset.prefetch_related("image")

        return queryset


class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    queryset = User.objects.all()


class TierViewSet(ReadOnlyModelViewSet):
    serializer_class = TierSerializer

    queryset = Tier.objects.all()


class ThumbnailViewSet(ReadOnlyModelViewSet):
    serializer_class = ThumbnailSerializer

    queryset = Thumbnail.objects.all()
