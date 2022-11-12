from M_app.web.models import Album, Profile
from django import forms


class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age',
                }),
        }


class DeleteProfile(forms.ModelForm):
    pass


class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owned',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Album name',
                }),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image Url',
                }),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                }),
        }


class AlbumDeleteForm(AlbumCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


class DeleteProfileForm(CreateProfile):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
