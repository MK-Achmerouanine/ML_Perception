from django.contrib import admin
from .models import Endpoint, ImageToTranslate, TextToAudio
from django.utils.html import format_html



class EndpointAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name','created_at', 'modified_at')
    list_filter = ('name',)
    
#admin.site.unregister(Endpoint) 
admin.site.register(Endpoint, EndpointAdmin)


# Image to translate

class ImageToTranslateAdmin(admin.ModelAdmin):
    list_display = ('image', 'camera','created_at',)
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag']
    readonly_fields = ['image_tag']
admin.site.register(ImageToTranslate, ImageToTranslateAdmin)

class TextToAudioAdmin(admin.ModelAdmin):
    list_display = ('audio', 'text','created_at',)
    
admin.site.register(TextToAudio, TextToAudioAdmin)