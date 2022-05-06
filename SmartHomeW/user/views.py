from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm


def register_user(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()

            messages.success(request, f'Пользователь был успешно создан.')
            return redirect('login')
    form = UserRegistrationForm()
    return render(request, 'user/../templates/user/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('sensors_home')
                else:
                    messages.error(request, f'Проблемы с аккаунтом. Создайте новый')
                    return redirect('register')
            else:
                messages.warning(request, f'Не удалось войти. Попробуйте еще раз.')
                return redirect('login')
    else:
        form = UserLoginForm()
    return render(request, 'user/../templates/user/login.html', {'form': form})


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return render(request, 'user/../templates/user/logout.html', {})
