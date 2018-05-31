from django.contrib.auth import get_user_model  # returns user model currently active
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        # these are the fields I want the user to fill out
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()  # gets the model of whoever is accessing the site

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        # sets up the <label> for the fields above. This is similar to manually making HTML labels
        self.fields['email'].label = 'Email Address'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'