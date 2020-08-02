from django.contrib import admin
from users.models import CustomUser
from .models import Enterprise
from settings.models import ProductType,ServiceType,Priority,Rate

admin.site.register(CustomUser)
admin.site.register(Enterprise)
admin.site.register(ProductType)
admin.site.register(Priority)
admin.site.register(Rate)
