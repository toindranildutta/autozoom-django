from django import forms
from .models import Location, Profile
from django.contrib.auth.models import User
from localflavor.us.forms import USZipCodeField
from .widget import CustomPictureImageFieldWidget


class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
    bio = forms.TextInput()

    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'phone_number')

class LocationForm(forms.ModelForm):
    address_1 = forms.CharField(required=True)
    pincode = USZipCodeField(required=True)
    
    class Meta:
        model = Location
        fields = '__all__'
