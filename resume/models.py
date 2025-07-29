from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    target_job = models.CharField(max_length=100)
    filename = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str({"name": self.name, "target_job": self.target_job, "filename": self.filename.name})

class Profile(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str({"title": self.title, "content": self.content[:50], "created_at": self.created_at})
