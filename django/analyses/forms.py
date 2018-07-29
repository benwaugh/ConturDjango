from django import forms
from .models import Document,Download,ufo_objects,runcard

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('upload_file',)

class DownloadForm(forms.ModelForm):
    class Meta:
        model = runcard
        fields = ('runcard_name','modelname','param_card','author',)

class UFOForm(forms.ModelForm):
    class Meta:
        model = ufo_objects
        fields = ('name','UFO_Link','author')

