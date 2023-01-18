from .models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'user_pic_profile')


class EditForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'user_pic_profile', 'name')
