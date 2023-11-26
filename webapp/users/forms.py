from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import PricePredictionInput
from django import forms



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

 
 
class PricePredictionForm(forms.ModelForm):
    class Meta:
        model = PricePredictionInput
        fields = ['Name', 'Quantity'] 


    
