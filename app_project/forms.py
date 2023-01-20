from django import forms
from .models import Projeto
from app_status.models import Status
from app_areas.models import Area
from app_user.models import User


class ProjetoForms(forms.ModelForm):
    titulo = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control col-10'}))
    inicio = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control col-4', 'type': 'date'}))
    fim = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control col-4', 'type': 'date'}))
    custo = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control col-3'}))
    status = forms.ModelChoiceField(queryset=Status.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control col-6'}))
    objetivo = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'content', 'name': 'body', 'rows': '5', 'cols': '3'}))
    area = forms.ModelMultipleChoiceField(queryset=Area.objects.all(),
                                          widget=forms.CheckboxSelectMultiple(
        attrs={'style': 'list-style: none; margin: 0;'}))
    integrantes = forms.ModelMultipleChoiceField(queryset=User.objects.all(),
                                                 widget=forms.CheckboxSelectMultiple(
                                                     attrs={'style': 'list-style: none; margin: 0;'}))
    responsavel = forms.ModelChoiceField(
        queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control col-6'}))
    # created_at = models.DateField(auto_now=True)
    # updated_at = models.DateField(auto_now_add=True)

    class Meta:
        model = Projeto
        exclude = ['created_at', 'updated_at']
