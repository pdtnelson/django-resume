from django.shortcuts import render, get_object_or_404
from .models import Resume
import json

def index(request):
    return render(request, 'resume/profile_view.html')

def resume_view(request):
    resume_model = get_object_or_404(Resume, pk=1)
    with resume_model.filename.open() as f:
        resume_data = json.loads(f.read())
    context = {'resume': resume_data}
    return render(request, 'resume/resume_view.html', context)
