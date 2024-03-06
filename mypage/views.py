from django.http import HttpResponse

def mypage(request):
    return HttpResponse("Its me!")