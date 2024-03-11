from django.http import HttpResponse
from .models import Person

def mypage(request):
    return HttpResponse("my page!")
    
    