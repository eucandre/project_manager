from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views.generic.detail import DetailView
from .forms import SignUpForm, EditForm
from .models import User


class UserView(DetailView):
    template_name = 'profile.html'

    def get_object(self):
        return self.request.user


def edit_profile(request, nr_id):
    object_user = User.objects.get(pk=nr_id)
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=object_user)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email,
                                password=raw_password)
            if user is not None:
                messages.success(
                    request, 'Salvo com Sucesso!')
                login(request, user)
            else:
                messages.error(request, "Não salvo")
                return redirect('users:profile')
            return redirect('users:profile')
        else:
            messages.error(request, "Não salvo")
    else:
        form = EditForm(instance=object_user)
    return render(request, 'edit_profile.html', {'form': form, 'pic': object_user.user_pic_profile.url if object_user.user_pic_profile else None})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'cli'  # Define a role como 'cli'
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("Usuário não autenticado!")
            return redirect('users:profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})