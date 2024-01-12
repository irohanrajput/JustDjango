from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('verify_otp/<str:user_id>/', verify_otp, name='verify_otp'),
    path('home/', home, name='home')
]
