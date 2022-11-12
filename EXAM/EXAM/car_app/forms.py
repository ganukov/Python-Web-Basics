from EXAM.car_app.models import Profile, Car
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class ProfileEdit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
