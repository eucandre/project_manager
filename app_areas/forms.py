from django import forms
from .models import Field

class FormField(forms.ModelForm):
    description = forms.CharField(label='Descrição',max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Field
        fields = '__all__'

class FormUpload(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))