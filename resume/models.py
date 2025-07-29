from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    target_job = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
