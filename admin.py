from django.contrib import admin
from .models import Image


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'description')


admin.site.register(Image, ImagesAdmin)
