from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages

from .forms import ProfileForm, LoginForm, CustomUserForm

User = get_user_model()


def login_view(request):
    if request.user.is_authenticated:
        print('1')
        return redirect('app1:home')

    form = LoginForm(request, data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)

        return redirect('app1:home')
    print(form.errors)
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.user.is_authenticated:
        return redirect('app1:home')

    form = CustomUserForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, "Ro‘yxatdan o‘tish muvaffaqiyatli! Iltimos, tizimga kiring.")
            return redirect('profil:login')
        else:
            messages.error(request, "Ro‘yxatdan o‘tishda xatolik bor! Iltimos, tekshirib qayta kiriting.")

    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('app1:home')


@login_required
def profil_view(request):
    user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profil:profil')
    else:
        form = ProfileForm(instance=user)

    return render(request, 'profil.html', {'form': form, 'user': user})


def account(request):
    if request.user.is_authenticated:
        return redirect('profil:profil')
    return render(request, 'account.html')
