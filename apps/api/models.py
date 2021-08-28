from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid


class Endpoint(models.Model):
    slug = models.SlugField(
        _("Slug"), default=uuid.uuid4(), blank=True, null=True)

    name = models.CharField(_("Name of the endpoint"), max_length=50)

    created_at = models.DateTimeField(
        _("Created at"), auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(
        _("Modified at"), auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = _("Endpoint")
        verbose_name_plural = _("Endpoints")

    def __str__(self):
        return self.name


class ImageToTranslate(models.Model):
    slug = models.SlugField(_("Slug"), default=uuid.uuid4())

    image = models.ImageField(_("Image"), upload_to="images_to_translate")
    text = models.TextField(_("Text"), blank=True, null=True)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified at"), auto_now=True)

    class Meta:
        verbose_name = _("Image to translate")
        verbose_name_plural = _("Images to translate")

    def __str__(self):
        return self.image.url

class ImageToAudio(models.Model):
    slug = models.SlugField(_("Slug"), default=uuid.uuid4())

    image = models.ImageField(_("Image"), upload_to="images_to_translate")
    audio = models.FileField(_("Audio"), upload_to="text_to_audio", blank=True, null=True)
    text = models.TextField(_("Text"), blank=True, null=True)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified at"), auto_now=True)

    class Meta:
        verbose_name = _("Image to audio")
        verbose_name_plural = _("Images to audio")

    def __str__(self):
        return self.image.url


class AudioToText(models.Model):
    slug = models.SlugField(_("Slug"), default=uuid.uuid4())
    audio = models.FileField(_("Audio"), upload_to="audio_to_text")
    text = models.TextField(_("Text"), blank=True, null=True)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified at"), auto_now=True)

    class Meta:
        verbose_name = _("Audio to text")
        verbose_name_plural = _("Audios to text")

    def __str__(self):
        return self.audio.url
        



class TextToAudio(models.Model):
    slug = models.SlugField(_("Slug"), default=uuid.uuid4())
    audio = models.FileField(_("Audio from text"), upload_to="text_to_audio", blank=True, null=True)
    text = models.TextField(_("Text"), blank=True, null=True)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified at"), auto_now=True)

    class Meta:
        verbose_name = _("Text to convert")
        verbose_name_plural = _("Texts to convert")

    def __str__(self):
        return self.audio.url


class TextToGcode(models.Model):
    slug = models.SlugField(_("Slug"), default=uuid.uuid4())
    gcode = models.TextField(_("Text"), blank=True, null=True)
    text = models.TextField(_("Text"), blank=True, null=True)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified at"), auto_now=True)

    class Meta:
        verbose_name = _("Text to convert")
        verbose_name_plural = _("Texts to convert")

    def __str__(self):
        return self.gcode.url
