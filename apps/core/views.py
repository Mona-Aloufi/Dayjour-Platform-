from django.shortcuts import render

def home(request):
 return render(request, "Blay/home.html") 
def login(request):
 return render(request, "login.html") 

