from django import forms
from .models import Download,runcard, BSM_Model,Analysis,AnalysisPool,attached_files,attached_papers


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Analysis
        fields = ('anaid','lumi','pool',)

class PoolForm(forms.ModelForm):
    class Meta:
        model = AnalysisPool
        fields = ('pool',)

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

class PaperForm(forms.ModelForm):
    class Meta:
        model = attached_papers
        fields = ('name','file',)

class FilesForm(forms.ModelForm):
    class Meta:
        model = attached_files
        fields = ('name','file',)