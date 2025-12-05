from django.urls import path
from .views import Signup, Login

urlpatterns = [
    path('Signup/', Signup.as_view(), name = 'auth_register'),
    path('Login/', Login.as_view(), name = 'auth_register')
]