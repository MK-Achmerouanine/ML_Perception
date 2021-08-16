from rest_framework import serializers
from .models import Endpoint, ImageToTranslate, TextToAudio, AudioToText


class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoint
        exclude = ('id',)


class ImageToTranslateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = ImageToTranslate
        exclude = ('id',)

class AudioToTextSerializer(serializers.ModelSerializer):
    audio = serializers.FileField()

    class Meta:
        model = AudioToText
        exclude = ('id',)

class TextToConvertSerializer(serializers.ModelSerializer):
    audio = serializers.FileField(required = False,allow_empty_file=True)

    class Meta:
        model = TextToAudio
        exclude = ('id',)
