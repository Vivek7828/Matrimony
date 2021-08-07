from django.shortcuts import render

# Create your views here.
def services(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')    

def signup(request):
    return render(request, 'core/signup.html')  