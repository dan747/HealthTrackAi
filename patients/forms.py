from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Patient, Doctor, Pharmacy

# ✅ Use get_user_model instead of importing CustomUser directly
CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('pharmacy', 'Pharmacy'),
    )

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'user_type',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = self.cleaned_data['user_type']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
            # Create profile based on user type
            if user.user_type == 'patient':
                Patient.objects.create(user=user)
            elif user.user_type == 'doctor':
                Doctor.objects.create(user=user)
            elif user.user_type == 'pharmacy':
                Pharmacy.objects.create(user=user)
        return user
