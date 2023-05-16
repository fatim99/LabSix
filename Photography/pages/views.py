from django.shortcuts import render
from .models import Contact

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        v_name = request.POST.get('name')
        v_email = request.POST.get('email')
        v_subject = request.POST.get('subject')
        v_massage = request.POST.get('massage')

        v_contact = Contact(name=v_name, email=v_email, subject=v_subject, massage=v_massage)
        v_contact.save()
        return render(request, 'pages/thanks.html')
    else:
        return render(request, 'pages/contact.html')
