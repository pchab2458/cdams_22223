from django import forms
from .models import TenantProfile, Room
from django.contrib.auth import get_user_model

CUser = get_user_model()


class TenantCreateForm(forms.ModelForm):
    password1 = forms.CharField(label='Password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput)

    class Meta:
        model = CUser
        fields = ('username', 'first_name', 'last_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    # def clean_email(self):
    #     data = self.cleaned_data['email']
    #     if CUser.objects.filter(email=data).exists():
    #         # if settings.AUTH_USER_MODEL.objects.filter(email=data).exists():
    #         raise forms.ValidationError('Email already in use.')
    #     return data


class TenantProfileCreateForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'pin', 'phone', 'term', 'start_date', 'deposit', 'adjust', 'extra'}


class PaymentForm(forms.Form):
    payment_amount = forms.DecimalField(max_digits=7, decimal_places=2,
                                        widget=forms.NumberInput(
                                            attrs={'class': 'paid_amount', 'placeholder': 'amount', 'min': 0}))
    payment_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'pay_date', 'placeholder': 'date'}))


class BookRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = {'status', 'exmovein_date'}

        widgets = {
            'status': forms.Select(attrs={'class': 'status'}),
            'exmovein_date': forms.DateInput(attrs={'class': 'exmovein_date', 'placeholder': 'date'})
        }


class Elec_cpu_change(forms.Form):
    elec_cpu = forms.DecimalField(max_digits=7, decimal_places=2,
                                  widget=forms.NumberInput(
                                      attrs={'class': 'elec_cpu', 'placeholder': 'elec_cpu', 'min': 0}))


class Water_cpu_change(forms.Form):
    water_cpu = forms.DecimalField(max_digits=7, decimal_places=2,
                                   widget=forms.NumberInput(
                                       attrs={'class': 'water_cpu', 'placeholder': 'water_cpu', 'min': 0}))


class BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0})
        }
