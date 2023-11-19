from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .views import predict_price
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    #path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('predict_price/', predict_price, name='predict_price'),
    path('admin/', admin.site.urls),
    #path('price_predictor/', include('price_predictor.urls')),
   

]