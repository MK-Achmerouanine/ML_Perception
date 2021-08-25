from rest_framework import viewsets
from django.http import HttpResponse
from .models import Endpoint, ImageToTranslate, TextToAudio, AudioToText, ImageToAudio
from .serializers import EndpointSerializer, ImageToTranslateSerializer, TextToConvertSerializer, ImageToAudioSerializer
from .serializers import AudioToTextSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.conf import settings 
from django.core.files.base import ContentFile
from django.core.files import File as DjangoFile
import pyttsx3
import os.path
import time




class EndpointViewSet(viewsets.ModelViewSet):
    queryset = Endpoint.objects.all()
    serializer_class = EndpointSerializer

    def list(self, request):
        queryset = Endpoint.objects.all()
        serializer = EndpointSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Endpoint.objects.all()
        endpoint = get_object_or_404(queryset, pk=pk)
        serializer = EndpointSerializer(endpoint)
        return Response(serializer.data)


class TextConvertedToAudioViewSet(viewsets.ModelViewSet):
    queryset = TextToAudio.objects.all()
    serializer_class = TextToConvertSerializer

    
    def post(self, request, *args, **kwargs):
        if not request.data['text']:
            return Response({'error': 'Bad Request'}, status=400)
        serializer = TextToConvertSerializer(data=request.data)
        if serializer.is_valid():
            print('Valid serializer')
            txt_to_convert = serializer.save()
            media_path = settings.MEDIA_ROOT
            print(f'Text to convert: {txt_to_convert.text}')

            engine = pyttsx3.init(driverName="espeak")
            #get voice properties
            voices = engine.getProperty('voices')
            for voice in voices:
                print("Voice:")
                print(" - ID: %s" % voice.id)
                print(" - Name: %s" % voice.name)
                print(" - Languages: %s" % voice.languages)
                print(" - Gender: %s" % voice.gender)
            #set some voice properties
            engine.setProperty('voice', "b'\\x02en-gb")   # use french for french
            engine.setProperty('rate', 130)
            
            dirname = f'{media_path}/trash/'
            filename = f'speech-{txt_to_convert.slug}.wav'
            engine.save_to_file(txt_to_convert.text, dirname+filename)
            engine.runAndWait()
            while not os.path.exists(dirname+filename):
                time.sleep(1)

            audio = open(dirname+filename, "rb")
            print(audio)
            django_file = DjangoFile(audio)
            txt_to_convert.audio.save(filename,django_file)
            audio.close()

            return Response(
                TextToConvertSerializer(
                    instance=txt_to_convert
                ).data,
                status=200
            )
        else:
            return Response({'error': f'Invalid Data: {serializer.errors}'}, status=400)

    def list(self, request):
        queryset = TextToAudio.objects.all()
        serializer = TextToConvertSerializer(queryset, many=True)
        return Response(serializer.data)


class ImageToTranslateViewSet(viewsets.ModelViewSet):
    queryset = ImageToTranslate.objects.all()
    serializer_class = ImageToTranslateSerializer

    def post(self, request, *args, **kwargs):
        # file = request.data['file']
        if not request.data['image']:
            return HttpResponse({'error': 'Bad Request'}, status=400)
        serializer = ImageToTranslateSerializer(data=request.data)
        if serializer.is_valid():
            img_to_trans = serializer.save()
            from .image_to_text import preprocess
            import pytesseract
            print(f'serializer path : {img_to_trans.image}')

            thresh = preprocess(f'media/{img_to_trans.image}')
            text = pytesseract.image_to_string(thresh, lang='eng')
            print(f'TEXT is {text}')
            img_to_trans.text = text
            img_to_trans.save()

            return Response(
                ImageToTranslateSerializer(
                    instance=img_to_trans
                ).data,
                status=200
            )
        else:
            return HttpResponse({'error': 'Invalid Data'}, status=400)

    def list(self, request):
        queryset = ImageToTranslate.objects.all()
        serializer = ImageToTranslateSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ImageToTranslate.objects.all()
        image_to_translate = get_object_or_404(queryset, pk=pk)
        serializer = ImageToTranslateSerializer(image_to_translate)
        return Response(serializer.data) 

class AudioToTextViewSet(viewsets.ModelViewSet):
    queryset = AudioToText.objects.all()
    serializer_class = AudioToTextSerializer

    def post(self, request, *args, **kwargs):
        print("9bel if: ", request.data['audio'])
        if not request.data['audio']:
            print("west if: ", request.data['audio'])
            return HttpResponse({'error': 'Bad Request'}, status=400)
        serializer = AudioToTextSerializer(data=request.data)
        if serializer.is_valid():
            audio_tobe_converted = serializer.save()
            print(audio_tobe_converted)
            from .audio_to_text import get_large_audio_transcription
            #print(f'serializer path : {img_to_trans.image}')
            text_result = get_large_audio_transcription(f'media/{audio_tobe_converted.audio}', 'en')
            print(f'TEXT is {text_result}')
            audio_tobe_converted.text = text_result
            audio_tobe_converted.save()
            # delete the content of audio_chunks folder after getting the text from audio
            mydir = 'media/trash/audio_chunks'
            for f in os.listdir(mydir):
                os.remove(os.path.join(mydir, f))
            
            return Response(
                AudioToTextSerializer(
                    instance=audio_tobe_converted
                ).data,
                status=200
            )
            
            
        else:
            return HttpResponse({'error': 'Invalid Data'}, status=400)

    def list(self, request):
        queryset = AudioToText.objects.all()
        serializer = AudioToTextSerializer(queryset, many=True)
        return Response(serializer.data)



class ImageToAudioViewSet(viewsets.ModelViewSet):
    queryset = ImageToAudio.objects.all()
    serializer_class = ImageToAudioSerializer

    def post(self, request, *args, **kwargs):
        # file = request.data['file']
        if not request.data['image']:
            return HttpResponse({'error': 'Bad Request'}, status=400)
        serializer = ImageToAudioSerializer(data=request.data)
        if serializer.is_valid():
            img_to_audio = serializer.save()
            from .image_to_text import preprocess
            import pytesseract
            print(f'serializer path : {img_to_audio.image}')
            media_path = settings.MEDIA_ROOT
            thresh = preprocess(f'media/{img_to_audio.image}')
            text = pytesseract.image_to_string(thresh, lang='eng')
            print(f'TEXT is {text}')
            engine = pyttsx3.init(driverName="espeak")
            #get voice properties
            voices = engine.getProperty('voices')
            for voice in voices:
                print("Voice:")
                print(" - ID: %s" % voice.id)
                print(" - Name: %s" % voice.name)
                print(" - Languages: %s" % voice.languages)
                print(" - Gender: %s" % voice.gender)
            #set some voice properties
            engine.setProperty('voice', "b'\\x02en-gb")   # use french for french
            engine.setProperty('rate', 130)

            import string    
            import random # define the random module  
            S = 5  # number of characters in the string.  
            # call random.choices() string module to find the string in Uppercase + numeric data.  
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
            print("The randomly generated string is : " + str(ran))

            dirname = f'{media_path}/trash/'
            filename = f'ImgSpeech-{str(ran)}.wav'
            engine.save_to_file(text, dirname+filename)
            engine.runAndWait()
            while not os.path.exists(dirname+filename):
                time.sleep(1)

            audio = open(dirname+filename, "rb")
            print(audio)
            django_file = DjangoFile(audio)
            img_to_audio.audio.save(filename,django_file)
            audio.close()
            img_to_audio.text = text
            img_to_audio.save()

            print(f'Filename BEFORE RESPONSE {filename}')
            return Response(
                ImageToAudioSerializer(
                    instance=img_to_audio
                ).data,
                status=200
            )
            
        else:
            return HttpResponse({'error': 'Invalid Data'}, status=400)

    def list(self, request):
        queryset = ImageToAudio.objects.all()
        serializer = ImageToAudioSerializer(queryset, many=True)
        return Response(serializer.data)

    