from django.shortcuts import render

def index(request):
    return render(request, 'donate/main.html' ,{})

def confirm(request):
    return render(request, 'donate/payment.html', {})