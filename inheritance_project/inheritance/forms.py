wlavoing
#from django import forms
#from .models import *

# class Artifact_form(forms.ModelForm):

# class Meta:
#model = Artifact
#fields = ['artifact_img']

from django import forms
from inheritance.models import Image



class ImageForm(forms.ModelForm):
    # Form for the image model
    class Meta:
        model = Image
        fields = ('title', 'image')
