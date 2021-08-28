from rest_framework import serializers
from .models import Endpoint, ImageToTranslate, TextToAudio, AudioToText, ImageToAudio, TextToGcode


class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoint
        exclude = ('id',)


class ImageToTranslateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = ImageToTranslate
        exclude = ('id',)


class ImageToAudioSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    #audio = serializers.FileField(required = False,allow_empty_file=True)
    class Meta:
        model = ImageToAudio
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


class TextToGcodeSerializer(serializers.ModelSerializer):
    gcode = serializers.CharField(required = False)

    class Meta:
        model = TextToGcode
        exclude = ('id',)
