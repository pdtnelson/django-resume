from django.shortcuts import render

def index(request):
    return render(request, 'resume/profile_view.html')
