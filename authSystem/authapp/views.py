from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import UserProfile
import random

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        def send_otp_email(email):
            otp = str(random.randint(100000, 999999))
            send_mail(
                subject="otp verification",
                message=f"sunn be bhadwe, tera otp likh {otp}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email], 
                fail_silently=False
                )
            return otp
        
        generated_otp=send_otp_email(email)
        user = UserProfile.objects.create(email=email, password=password, generated_otp=generated_otp) 
        #save user data in the database including the generated otp

        return redirect('verify_otp', user_id=user.id)
        #pass the user's unique id to the 'verify_otp' view that will be used to fetch data in that view.
    
    return render(request, 'signup.html')

def verify_otp(request, user_id):
    user = UserProfile.objects.get(id=user_id) 
    #fetch user details from the database that contains generated otp too, for the verification.
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        if entered_otp == user.generated_otp:
            #now we can write our code here for login, authentication and whatever the hell you want to.
            return redirect('home')
        else:
            return HttpResponse("Invalid OTP")
    user.generated_otp = ''
    #delete the generated otp once verification is done if you wnat to, go find yourself how to do it, that's it for now. sayonara
    return render(request, 'otp.html', {'user_id': user.id})

def home(request):
    return render(request, 'home.html')