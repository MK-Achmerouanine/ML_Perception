from django.urls import path
from .views import EndpointViewSet, ImageToTranslateViewSet
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
]
