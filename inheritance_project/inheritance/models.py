
from django.db import models

# Create your models here.

from django.urls import reverse  # To generate URLS by reversing URL patterns


class artifacts(models.Models):
    artifact_title = models.CharField(
        max_length=50, help_text='Enter name of Artifact')
    artifact_summary = models.CharField(
        max_length=250, help_text='Enter description of Artifact')
    inheritance_date = models.DateField()
    contributor = models.CharField(max_length=50, help_text='Enter your name')
    artifact_image = BLOB
    access_key = ()  # access_key assignment to be determined


def _str_(self):
    return self.artifacts
