from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User, Image, Thumbnail, Tier


class UserAdminNew(UserAdmin):
    fieldsets = ((None, {"fields": ("username", "password", "tier")}),)


admin.site.register(User, UserAdminNew)
admin.site.register(Image)
admin.site.register(Thumbnail)
admin.site.register(Tier)
admin.site.unregister(Group)
