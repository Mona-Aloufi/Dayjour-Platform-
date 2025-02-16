from django.shortcuts import render

def home(request):
 return render(request, "Blay/home.html") 
def login_view(request):
    return render(request, 'login.html')
def signin_view(request):
    return render(request, 'signin.html')

def dashboard(request):
    return render(request, 'dashboard.html')

