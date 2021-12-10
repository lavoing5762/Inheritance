# Required for unique artiface instances.  Example, black and white filtering, sepia_tone, and color.  Creates unique id for artifact.
import uuid
from django.db import models
from django.db.models.deletion import RESTRICT
from django.urls import reverse
# Create your models here.



# To generate URLS by reversing URL patterns


class Artifact(models.Model):
    artifact_title = models.CharField(
        max_length=25, help_text='Enter name of Artifact')
    #artifact_img = models.ImageField(upload_to='images')

    artifact_type = (

        ('heirloom', 'HEIRLOOM'),
        ('inspirational', 'INSPIRATIONAL'),
        ('educational', 'EDUCATIONAL'),
        ('emotional', 'EMOTIONAL'),
        ('wisdom', 'WISDOM'),
        ('abstract', 'ABSTRACT'),
        ('culture', 'CULTURAL'),
        ('political', 'POLITICAL'),
        ('national', 'NATIONAL'),
        ('graphical', 'GRAPHICAL'),
        ('musical', 'MUSICAL'),
        ('lyrical', 'LYRICAL'),
        ('poetic', 'POETIC'),
        ('beautiful', 'BEAUTIFUL'),
        ('complimentary', 'COMPLIMENTARY'),
        ('foundational', 'FOUNDATIONAL'),
        ('indulgent', 'INDULGENT'),
        ('decadent', 'DECADENT'),
        ('comforting', 'COMFORTING'),
        ('luxurious', 'LUXURIOUS'),
        ('basic', 'BASIC'),
        ('historical', 'HISTORICAL'),
        ('illuminating', 'ILLUMINATING'),
        ('nuturing', 'NUTUTRING'),
        ('intellectual', 'INTELLECTUAL'),
        ('fashionable', 'FASHIONABLE'),
        ('entertainment', 'ENTERTAINMENT')
    )

    artifact_summary = models.CharField(
        max_length=250, help_text='Enter description of Artifact')
    inheritance_date = models.DateField(
        help_text='Enter committment of artifact date')
    contributor_name = models.CharField(
        max_length=50, help_text='Enter your name')
    artifact_image = models.TextField()
    # access_key assignment to be determined
    access_key = models.CharField(max_length=50)

    def get_absolute_url(self):
        # Returns the url to access a detail record for the artifact.
        return reverse("artifacts_detail", kwargs={"pk": self.pk})

    class Meta:
        db_table = 'artifact'
        # ordering = ['']  # Sort by field name.

    def _str_(self):
        return self.Artifact


class Artifact_Instance(models.Model):
    select_filter = (
        ('original', 'ORIGINAL'),
        ('b&w', 'B&W'),
        ('sepia', 'SEPIA'),
        ('color', 'COLOR')
    )
    artifact = models.ForeignKey(
        'Artifact', on_delete=models.RESTRICT, null=True)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

    class Meta:
        db_table = 'artifact_instance'
        # ordering = ['']  # Sort by field name.

    def __str__(self):
        return f'uuid'.artifact_instance


class Contributor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    artifact = models.ForeignKey(
        'Artifact', on_delete=models.RESTRICT, null=True)

    class Meta:
        db_table = 'contributor'
        # ordering = ['']  # Sort by field name.

    def get_absolute_url(self):
        # Returns the url to access a particular author instance
        return reverse("contributor_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

# This class is to upload the image   
class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title
    class Meta:
        db_table = "myapp_image"
