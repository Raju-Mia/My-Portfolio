from django.shortcuts import render
from .models import AboutMe

# Create your views here.


def home(request):
    aboutmeall = AboutMe.objects.get(id=1)
    print(aboutmeall.age)
    context = {'about': aboutmeall}
    print("hello")
    return render(request, 'index.html', context)