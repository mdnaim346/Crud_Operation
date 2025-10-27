from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Naim! Welcome to your first Django app 🎉")
