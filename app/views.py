from django.shortcuts import render, HttpResponse
from controller import temp_mail

def index(requests):
    email = temp_mail.email.address
    return render(requests, "main.html", {"email": email})