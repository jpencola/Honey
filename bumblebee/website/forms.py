from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    name = forms.CharField(max_length=64)
    difficulty = forms.IntegerField()