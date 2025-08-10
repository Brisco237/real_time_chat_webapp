from django.shortcuts import render

# Create your views here.
def login_user(request):
    return render(request, 'authapp/login.html')

def register_user(request):
    return render(request, 'authapp/register.html')
