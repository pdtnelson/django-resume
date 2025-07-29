from django.http import HttpResponse

def index(request):
    return HttpResponse("Hell from resume index page!")
