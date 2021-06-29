"""HexOcean URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db.models import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.views import ImageViewSet, ThumbnailViewSet, UserViewSet, TierViewSet
from django.conf.urls import url, include
from .settings import *
from django.views.static import serve

router = DefaultRouter()
router.register(r"image", ImageViewSet, basename="Image")
router.register(r"user", UserViewSet, basename="User")
router.register(r"thumbnail", ThumbnailViewSet, basename="Thumbnail")
router.register(r"tier", TierViewSet, basename="Tier")

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("backend/", include("backend.urls")),
    url(r"^admin/", admin.site.urls),
    url(r"^", include(router.urls)),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': MEDIA_ROOT, })
]
