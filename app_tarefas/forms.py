from django import forms
from .models import Task
from app_user.models import User
from app_status.models import Status


class FormTask(forms.ModelForm):
    title = forms.CharField(max_length=255, label='Titulo', widget=forms.TextInput(attrs={'class':'form-control'}))
    cost = forms.FloatField(label='Valor', widget=forms.TextInput(attrs={'class':'form-control'}))
    status = forms.ModelChoiceField(label='Status',queryset=Status.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    responsable = forms.ModelChoiceField(label='Responsável',queryset=User.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    dependencies = forms.CharField(max_length=255, label='Dependências', widget=forms.TextInput(attrs={'class':'form-control'}))
    attachment = forms.FileField(label='Anexo')
    start = forms.DateField(label='Início',widget=forms.TextInput(attrs={'type':'date', 'class':'form-control'}))
    end = forms.DateField(label='Fim',widget=forms.TextInput(attrs={'type':'date', 'class':'form-control'}))
    goals = forms.CharField(label='Objetivos',max_length=3000, widget=forms.Textarea(attrs={'class':'styled-textarea'}))
    class Meta:
        model = Task
        fields = ['title', 'goals', 'cost', 'status', 'responsable', 'dependencies', 'attachment', 'start', 'end']

    def __init__(self, *args, **kwargs):
        super(FormTask, self).__init__(*args, **kwargs)
        # Filtra apenas os usuários com a role "cli"
        self.fields['responsable'].queryset = User.objects.filter(role='cli')
        
    