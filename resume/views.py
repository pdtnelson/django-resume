from django.shortcuts import render

def index(request):
    return render(request, 'resume/profile_view.html')

def resume_view(request):
    # For now, we will just render a static template
    return render(request, 'resume/resume_view.html')
