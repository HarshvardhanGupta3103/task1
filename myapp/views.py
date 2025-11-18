from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def home(request):
    projects = Project.objects.all()
    clients = Client.objects.all()
    return render(request, 'index.html', {'projects': projects, 'clients': clients})


def contact_submit(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        city = request.POST.get("city")

        # Check duplicate email
        if Contact.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered!")
            return redirect("index")

        # Save new contact
        Contact.objects.create(
            full_name=full_name,
            email=email,
            mobile_number=mobile,
            city=city
        )

        messages.success(request, "Your contact form has been submitted successfully!")

    return redirect("index")




def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get("email")

        # Check Empty Email  
        if not email:
            messages.error(request, "Please enter an email address.")
            return redirect("index")

        # Duplicate Email
        if Newsletter.objects.filter(email=email).exists():
            messages.warning(request, "This email is already subscribed!")
            return redirect("index")

        # Save to DB
        Newsletter.objects.create(email=email)
        messages.success(request, "Thank you for subscribing!")

    return redirect("index")
