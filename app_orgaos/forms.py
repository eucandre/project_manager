from django import forms
from .models import Organ


class Orgaoform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Orgaoform, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['cep'].widget.attrs['class'] = 'form-control'
        self.fields['acronym'].widget.attrs['class'] = 'form-control'
        self.fields['active'].widget.attrs['class'] = 'form-control'
        self.fields['website'].widget.attrs['class'] = 'form-control'
        self.fields['whatsapp'].widget.attrs['class'] = 'form-control'
        self.fields['chef'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Organ
        fields = '__all__'
        exclude = ['id', 'created_at', 'updated_at', 'lattitude', 'longitude']
