from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user','bio','location','birth_date','school_affiliate','national_identification_number','country_of_origin','current_country_or_residence','current_county','current_city','level_of_education','first_name','last_name','avatar','slug','receive_newsletter',]

