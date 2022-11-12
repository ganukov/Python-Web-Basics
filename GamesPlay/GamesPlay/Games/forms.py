from GamesPlay.Games.models import Profile, Game
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'email': forms.EmailInput(),
            'age': forms.NumberInput(),
            'password': forms.PasswordInput(),
        }


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'




class GameDeleteForm(GameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
