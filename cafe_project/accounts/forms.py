from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views import View
from .models import Booking


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello World!')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["client", "number", "date", "start time", "end time", "guests count"]