from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class EmployeeSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

