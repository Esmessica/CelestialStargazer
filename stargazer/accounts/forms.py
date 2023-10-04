from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):

    class Meta:
        field = ('username', 'email', 'password1', 'password2')
        model = get_user_model()
        #   model of user accessing our website

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Stargazer's name"
        self.fields['email'].label = 'Email Address'
        #  set up labels for forms
