# Register your models here.
from django.contrib import admin
from .models import Image
from .models import Artifact, Artifact_Instance, Contributor




admin.site.register(Artifact)
admin.site.register(Artifact_Instance)
admin.site.register(Contributor)
admin.site.register(Image)  # Register for Image Uploader
