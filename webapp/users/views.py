from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from .forms import PricePredictionForm
from .models import CustomUser
from .models import PricePredictionInput
from django.contrib import messages


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
import re

import joblib
# price_predictor/views.py
from django.shortcuts import render
from .forms import PricePredictionForm



# Load the pre-trained model outside the view function
model = joblib.load('C:/Users/user/Documents/GitHub/135399/webapp/models/linear_regression_model.h5')

def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

model = joblib.load('C:/Users/user/Documents/GitHub/135399/webapp/models/linear_regression_model.h5')

def preprocess_data(data):
   X = data[['Name', 'Price Per Each', 'Quantity']]
   y = data['Current Price KSH']

   # Encode categorical variables
   le_name = LabelEncoder()
   X['Name'] = le_name.fit_transform(X['Name'])

    # Convert 'Quantity' to numeric, handling cases with units
   def extract_numeric(value):
       try:
           return float(re.search(r'\d+\.*\d*', value).group())
       except (AttributeError, ValueError):
           return 1.0
       
   X['Quantity'] = X['Quantity'].apply(extract_numeric)

   imputer = SimpleImputer(strategy='mean')
   X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

   return X_imputed, y
    
          
def predict_price(request):
    form = PricePredictionForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user_input = form.cleaned_data

        # Prepare the user input for prediction
        input_data = pd.DataFrame({
            'Name': [user_input['Name']],
            'Price Per Each': [user_input['Price Per Each']],
            'Quantity': [user_input['Quantity']]
        })

        # Load the pre-trained model
        #model = joblib.load('C:/Users/user/Documents/GitHub/135399/webapp/models/linear_regression_model.h5')

        # Prepare the user input for prediction
        X = [[user_input['Name'], user_input['Quantity']]]


        # Use the model for prediction
        predicted_price = model.predict(X)

        context = {'form': form, 'predicted_price': predicted_price}
        return render(request, 'users/result.html', context)

    context = {'form': form}
    return render(request, 'users/predict_price.html', context)

# Load your training data
# Assuming 'product_data.csv' is your dataset file
file_path = 'C:/Users/user/Documents/GitHub/135399/webapp/product_data.csv'
data = pd.read_csv("C:/Users/user/Documents/GitHub/135399/webapp/products_data (1).csv")

# Preprocess the data
X_train, y_train = preprocess_data(data)

# Fit the model with the training data
model.fit(X_train, y_train)


