
# Required for unique artiface instances.  Example, black and white filtering, sepia_tone, and color.  Creates unique id for artifact.
import uuid
from django.db import models
from django.db.models.deletion import RESTRICT

# Create your models here.

from django.urls import reverse

# To generate URLS by reversing URL patterns


class artifacts(models.Models):
    artifact_title = models.CharField(
        max_length=25, help_text='Enter name of Artifact')

    artifact_type = (

        ('heirloom', 'HEIRLOOM'), ('inspirational', 'INSPIRATIONAL'), ('educational', 'EDUCATIONAL'), ('emotional', 'EMOTIONAL'), ('wisdom', 'WISDOM'), ('abstract', 'ABSTRACT'), ('culture', 'CULTURAL'), ('political', 'POLITICAL'), ('national', 'NATIONAL'), ('graphical', 'GRAPHICAL'), ('musical', 'MUSICAL'), ('lyrical', 'LYRICAL'), ('poetic', 'POETIC'), ('beautiful',
                                                                                                                                                                                                                                                                                                                                                                    'BEAUTIFUL'), ('complimentary', 'COMPLIMENTARY'), ('foundational', 'FOUNDATIONAL'), ('indulgent', 'INDULGENT'), ('decadent', 'DECADENT'), ('comforting', 'COMFORTING'), ('luxurious', 'LUXURIOUS'), ('basic', 'BASIC'), ('historical', 'HISTORICAL'), ('illuminating', 'ILLUMINATING'), ('nuturing', 'NUTUTRING'), ('intellectual', 'INTELLECTUAL'), ('fashionable', 'FASHIONABLE'), ('entertainment', 'ENTERTAINMENT')
    )

    artifact_summary = models.CharField(
        max_length=250, help_text='Enter description of Artifact')
    inheritance_date = models.DateField(
        help_text='Enter committment of artifact date')()
    contributor = models.CharField(max_length=50, help_text='Enter your name')
    artifact_image = models.TextField()
    # access_key assignment to be determined
    access_key = models.CharField(max_length=50)

    def get_absolute_url(self):
        # Returns the url to access a detail record for the artifact.
        return reverse("artifacts_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['']  # Sort by field name.

    def _str_(self):
        return self.artifacts


class artifact_instance(models.Model):
    select_filter = (
        ('original', 'ORIGINAL'), ('b&w', 'B&W'), ('sepia', 'SEPIA'), ('color', 'COLOR'))
    artifact = models.ForeignKey(
        'Artifact', on_delete=models.RESTRICT, null=True)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['']  # Sort by field name.

    def __str__(self):
        return f'uuid'.artifact_instance


class contributor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    artifact = models.ForeignKey(
        'Artifact', on_delete=models.RESTRICT, null=True)

    class Meta:
        ordering = ['']  # Sort by field name.

    def get_absolute_url(self):
        # Returns the url to access a particular author instance
        return reverse("contributor_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
