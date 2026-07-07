from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models import Profile
from .models import Room
from .models import ContactMessage


class RegisterForm(forms.ModelForm):

    full_name = forms.CharField(
        max_length=100,
        label="Full Name"
    )

    phone = forms.CharField(
        max_length=20,
        label="Phone Number"
    )

    role = forms.ChoiceField(
        choices=Profile.ROLE_CHOICES
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput
    )

    class Meta:

        model = User

        fields = (
            "username",
            "email",
        )

    def clean(self):

        cleaned_data = super().clean()

        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")

        if p1 != p2:

            raise forms.ValidationError(
                "Passwords do not match."
            )

        return cleaned_data


class LoginForm(AuthenticationForm):

    username = forms.CharField()

    password = forms.CharField(
        widget=forms.PasswordInput
    )


class RoomForm(forms.ModelForm):

    class Meta:

        model = Room

        fields = (
            "title",
            "description",
            "room_type",
            "price",
            "location",
            "phone",
            "image",
            "available",
        )

        widgets = {

            "description":
            forms.Textarea(
                attrs={
                    "rows":4
                }
            ),

        }


class ContactForm(forms.ModelForm):

    class Meta:

        model = ContactMessage

        fields = (
            "message",
        )

        widgets = {

            "message":
            forms.Textarea(
                attrs={
                    "rows":5
                }
            ),

        }
