from django import forms
from .models import Project
from app_status.models import Status
from app_areas.models import Field
from app_user.models import User


class ProjetoForms(forms.ModelForm):
    title = forms.CharField(label='Título', max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control col-10'}))
    start = forms.DateField(label='Início', widget=forms.DateInput(
        attrs={'class': 'form-control col-4', 'type': 'date'}))
    end = forms.DateField(label='Fim',widget=forms.DateInput(
        attrs={'class': 'form-control col-4', 'type': 'date'}))
    cost = forms.CharField(label='Custo', max_length=15, widget=forms.NumberInput(
        attrs={'class': 'form-control col-3'}))
    status = forms.ModelChoiceField(label='Status',queryset=Status.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control col-6'}))
    gols = forms.CharField(label='Objetivo',widget=forms.Textarea(
        attrs={'class': 'form-contol mt-2 styled-textarea'}))
    field = forms.ModelMultipleChoiceField(label='Área',queryset=Field.objects.all(),
                                          widget=forms.CheckboxSelectMultiple(
        attrs={'style': 'list-style: none; margin: 0;'}))
    mebmers = forms.ModelMultipleChoiceField(label='Membros',queryset=User.objects.all(),
                                                 widget=forms.CheckboxSelectMultiple(
                                                     attrs={'style': 'list-style: none; margin: 0;'}))
    responsable = forms.ModelChoiceField(label='Responsável Pelo Projeto',
        queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control col-6'}))
    attachment = forms.FileField(label='Anexo')


    class Meta:
        model = Project
        exclude = ['created_at', 'updated_at']
