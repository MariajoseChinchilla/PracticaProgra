from django import forms
from .models import UploadedFiles

class FileForm(forms.ModelForm):
    class Meta:
        model = UploadedFiles
        fields = ['title','p2']

