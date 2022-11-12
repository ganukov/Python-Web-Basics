from Music_app.my_app.models import Profile, Album
from django import forms

CHOICES = ["Pop Music", "Jazz Music", "R&B Music", "Rock Music", "Country Music", "Dance Music", "Hip Hop Music",
           "Other"]


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Username', }
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Email', }
            ),
            'age': forms.NumberInput(
                attrs={'placeholder': 'Age', }
            ),

        }


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={'placeholder': 'Album Name', }
            ),
            'artist': forms.TextInput(
                attrs={'placeholder': 'Artist', }
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Description', }
            ),
            'image_url': forms.URLInput(
                attrs={'placeholder':'Image URL',}
            ),
            'price': forms.NumberInput(
                attrs={'placeholder':'Price',}
            ),

        }
