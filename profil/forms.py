from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class CustomUserForm(UserCreationForm):
    username = forms.CharField(label="Foydalanuvchi nomi", max_length=150)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Parol", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Parolni tasdiqlang", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu email allaqachon ro‘yxatdan o‘tgan!")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Parollar mos kelmadi! Iltimos, qayta tekshiring.")

        return cleaned_data


class ProfileForm(forms.ModelForm):
    username = forms.CharField(label="Foydalanuvchi nomi", max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label="Telefon raqam", required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="Ism", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Familiya", required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'first_name', 'last_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("Bu email allaqachon band!")
        return email


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Foydalanuvchi nomi",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Foydalanuvchi nomingizni kiriting'})
    )
    password = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parolingizni kiriting'})
    )
