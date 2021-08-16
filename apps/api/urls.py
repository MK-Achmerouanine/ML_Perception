from django.urls import path
from .views import EndpointViewSet, ImageToTranslateViewSet, TextConvertedToAudioViewSet, AudioToTextViewSet
app = 'api'

urlpatterns = [
    path('endpoint/',
         EndpointViewSet.as_view({'get': 'list'}),
         name="endpoint-list"),
    path('endpoint/<pk>/',
         EndpointViewSet.as_view({'get': 'retrieve'}),
         name="endpoint-retrieve"),
    path('image_to_translate/', ImageToTranslateViewSet.as_view(
        {'get': 'list', 'post': 'post'}),
        name="image-to-translate"),
    path('image_to_translate/<pk>/', ImageToTranslateViewSet.as_view(
        {'get': 'retrieve'}),
        name="image-to-translate-retrieve"),
    #Text to speech 
    path('text_to_audio/', TextConvertedToAudioViewSet.as_view(
        {'get': 'list', 'post': 'post'}),
        name="text_to_audio"),

    #Speech to text
    path('audio_to_text/', AudioToTextViewSet.as_view(
        {'get': 'list', 'post': 'post'}),
        name="audio_to_text"),
    
]
