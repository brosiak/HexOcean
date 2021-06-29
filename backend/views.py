# from django.shortcuts import render
# from django.http import JsonResponse

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import ImageSerializer
# from .models import *

# @api_view(['GET'])
# def api_overview(request):
#     return JsonResponse("API BASE POINT", safe=False)

# @api_view(['GET'])
# def image_list(request):
#     images = Image.objects.all()
#     serializer = ImageSerializer(images, many=True)

#     return Response(serializer.data)

from rest_framework.decorators import action
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ImageSerializer, ThumbnailSerializer, TierSerializer, UserSerializer
from .models import Image, User, Thumbnail, Tier
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_flex_fields import is_expanded
from django_filters import rest_framework as filters

class ImageViewSet(FlexFieldsModelViewSet):
    serializer_class = ImageSerializer
    permit_list_expands = ["user", "image"]
    filterset_fields = ("user", )

    def get_queryset(self):
        queryset = Image.objects.all()
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
