from django import forms
from .models import Document,Download,runcard, BSM_Model,Analysis


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
        model = BSM_Model
        fields = ('name','UFO_Link','author')

class AnalysesForm(forms.Form):

    OPTIONS = Analysis.objects.all()
    opts = []
    for value in OPTIONS:
        opts.append(tuple([value,value]))
    name = forms.CharField()
    author = forms.CharField()
    analyses = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=opts)
