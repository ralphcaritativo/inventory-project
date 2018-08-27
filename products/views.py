from django.shortcuts import render

def login(request):
    return render(request, 'products/login.html')



def dashboard(request):
    return render(request, 'products/dashboard.html')
