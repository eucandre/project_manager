from django import forms
from .models import Function


class FormFuncion(forms.ModelForm):
    description = forms.CharField(max_length=255, label='Descrição', widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Function
        fields = '__all__'