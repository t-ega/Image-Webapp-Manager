from rest_framework import serializers
from .models import Images


class ImageSerializer(serializers.ModelSerializer):
    model = Images
    fields = '__all__'
