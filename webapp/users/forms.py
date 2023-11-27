from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import PricePredictionInput
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

 
 
class PricePredictionForm(forms.ModelForm):
    class Meta:
        model = PricePredictionInput
        fields = ['Name', 'Quantity'] 

    def save_prediction(self, user):
        # Save the prediction to the database
        prediction = super().save(commit=False)
        prediction.user = user
        prediction.predicted_price = self.calculate_predicted_price()  # You need to implement this method
        prediction.save()
        return prediction
    
        
class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
                model = CustomUser
                fields = ('username', 'email', 'first_name', 'last_name', 'other_fields_if_any')
    pass
    # You can customize this form if needed
   
class CustomUserChangeForm(UserChangeForm):
     class Meta:
          pass