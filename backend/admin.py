from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import *

admin.site.register(User)  # , UserAdmin)
admin.site.register(Image)
admin.site.register(Thumbnail)
admin.site.register(Tier)

admin.site.unregister(Group)
