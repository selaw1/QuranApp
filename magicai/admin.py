from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from magicai.models import ResponseData, UserPrompt

admin.site.register(UserPrompt)
admin.site.register(ResponseData)


