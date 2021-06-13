from django.shortcuts import render
from django.http import HttpResponse
from .models import Kontakt, SliderInfo, About
from django.core.mail import send_mail



def home_pg(request):
    slider_content_1 = SliderInfo.objects.filter(id=1)
    slider_content_2 = SliderInfo.objects.filter(id=2)
    slider_content_3 = SliderInfo.objects.filter(id=3)
    slider_content_4 = SliderInfo.objects.filter(id=4)
    about = About.objects.all()
    return render(request, 'main/index.html', {'slider_content1': slider_content_1, 'slider_content2': slider_content_2, 'slider_content3': slider_content_3, 'slider_content4': slider_content_4, 'about': about})

def about(request):
    kontakt = Kontakt.objects.all()
    return render(request, 'main/kontakt.html', {'kontakt': kontakt})


def feedback(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        notification = 'Your email is sent'


        send_mail(
            'Tagasiside/küsimus: ' + message_name + ', ' + message_email, # subject
            message, # message
            message_email, # from email
            ['pavelantonov1134@gmail.com'], # To email
        )
        return render(request, 'main/feedback.html', {'notification': notification})

    else:
        return render(request, 'main/feedback.html', {})

