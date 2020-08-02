from django.contrib import admin
from users.models import CustomUser
from .models import Enterprise

admin.site.register(CustomUser)
admin.site.register(Enterprise)