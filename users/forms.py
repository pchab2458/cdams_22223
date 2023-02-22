from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # Default
    # class Meta(UserCreationForm.Meta):
    #     model = CustomUser
    #     fields = UserChangeForm.Meta.fields

    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields
        fields = ('username', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
