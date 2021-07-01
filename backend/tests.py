from django.http import request
from rest_framework.test import force_authenticate, APIRequestFactory, APITestCase
from .models import User, Image, Tier, Thumbnail
from .views import ImageViewSet


USER_NAMES = ["basic", "medium", "pro", "admin"]

TIER_VARIABLES = {
    "basic": [False, False],
    "medium": [True, False],
    "pro": [True, True],
    "admin": [True, False],
}

THUMBNAILS = {"200": ["basic"], "400": ["medium", "pro", "admin"]}


def test_setup():
    TV = TIER_VARIABLES
    for tier in USER_NAMES:
        Tier(name=tier, has_url=TV.get(tier)[0], can_fetch_url=TV.get(tier)[1]).save()
    for name in USER_NAMES:
        User(username=name, password=name, tier=Tier.objects.get(name=name)).save()
    for thumbnail in THUMBNAILS:
        tn = Thumbnail(name=thumbnail, size=int(thumbnail))
        tn.save()
        for tier in THUMBNAILS.get(thumbnail):
            tn.tiers.add(Tier.objects.get(name=tier))
    # for user in User.objects.all():
    #     for _ in range(2):
    #         Image(name=_+user.username, user=User.objects.get())


class ImageTests(APITestCase):
    def test_image_get(self):
        test_setup()
        user = User(username="tom", password="tom")
        user.save()
        factory = APIRequestFactory()
        user = User.objects.get(username="tom")
        # view = ImageViewSet.as_view({'get': 'list'})

        # Make an authenticated request to the view...
        # request = factory.get('/image/')
        # force_authenticate(request, user=user)
        # response = view(request)
        # factory = APIRequestFactory
