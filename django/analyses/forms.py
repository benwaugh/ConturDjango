from django import forms
from .models import Document,Download

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('upload_file',)

class DownloadForm(forms.ModelForm):
    class Meta:
        model = Download
        fields = ('runcard_name','Model','Parameter_Card',)
