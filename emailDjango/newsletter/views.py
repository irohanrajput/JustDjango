from django.shortcuts import render
from django.core.mail import send_mail
from .forms import emailForm
from django.conf import settings

def newsletter_signup(request):
    if request.method == 'POST':
        form = emailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            send_mail(
                subject="Hellooooo",
                message="See, life is good. Trust me on this and keep flying. ",
                from_email=settings.DEFAULT_FROM_EMAIL, 
                recipient_list=[email], 
                fail_silently=False,
            )
            return render(request, 'success.html')
    else:
        form = emailForm()
    return render(request, 'signup.html', {'form': form})
