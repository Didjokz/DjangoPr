from django.http import HttpResponse
from .models import Person

def mypage(request):
    objects = Person.objects.all()
    
    