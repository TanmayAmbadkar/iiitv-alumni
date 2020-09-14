from django import forms
from alumni.models import *

class AlumniForm(forms.ModelForm):

    class Meta:
        model = Alumni
        fields = __all__
