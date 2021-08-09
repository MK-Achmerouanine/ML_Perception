from rest_framework import serializers
from .models import Endpoint, ImageToTranslate


class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoint
        exclude = ('id',)


class ImageToTranslateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = ImageToTranslate
        exclude = ('id',)
