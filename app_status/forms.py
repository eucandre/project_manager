from django import forms
from .models import Status


class FormStatus(forms.ModelForm):
    description = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Status
        fields = '__all__'