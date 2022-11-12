from django import forms


class NameForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        help_text='Enter your Name',
        widget=forms.TextInput(
            # HTML ATTRIBUTES
            attrs={
                'placeholder': 'Enter name',
                'class': 'form-control',
            }
        )
    )

    age = forms.IntegerField(
        required=False,
        help_text='Enter your Age')
    email = forms.CharField(
        widget=forms.EmailInput(),

    )
    url = forms.CharField(
        widget=forms.URLInput(),
    )
    secret = forms.CharField(
        widget=forms.PasswordInput(),
    )
    OCCUPANCIES = (
        (1, 'Child'),
        (2, 'High School studend'),
        (3, 'Student'),
        (4, 'Adult'),
    )
    occupancy = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.RadioSelect(),
    )
