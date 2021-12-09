from django.contrib import admin

# Register your models here.
from .models import Artifact, Artifact_Instance, Contributor

admin.site.register(Artifact)
admin.site.register(Artifact_Instance)
admin.site.register(Contributor)
