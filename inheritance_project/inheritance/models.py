
# Required for unique artiface instances.  Example, black and white filtering, sepia_tone, and color.  Creates unique id for artifact.
import uuid
from django.db import models
from django.db.models.deletion import RESTRICT

# Create your models here.

from django.urls import reverse

# To generate URLS by reversing URL patterns


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


def get_absolute_url(self):
    # Returns the url to access a detail record for the artifact.

    return reverse("artifacts_detail", kwargs={"pk": self.pk})


class artifact_instance(models.Model):
    black_and_white = models.CharField(max_length=50)
    sepia_tone = models.CharField(max_length=50)
    color_artifact = models.CharField(max_length=50)
    artifact = models.ForeignKey(
        'Artifact', on_delete=models.RESTRICT, null=True)


def __str__(self):
    return f'uuid'.artifact_instance


class contributor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        # Returns the url to access a particular author instance
        return reverse("contributor_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
