from django import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from .models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'user_pic_profile')


class EditForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"class": "form-control"})
        self.fields["user_pic_profile"].widget.attrs.update(
            {"class": "form-control"})
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["function_in_the_project"].widget.attrs.update(
            {"class": "form-control"})
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control"})
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control"})

    class Meta:
        model = User
        fields = ('email', 'user_pic_profile',
                  'name', 'function_in_the_project')
