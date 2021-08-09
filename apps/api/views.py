from rest_framework import viewsets
from django.http import HttpResponse
from .models import Endpoint, ImageToTranslate
from .serializers import EndpointSerializer, ImageToTranslateSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


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
