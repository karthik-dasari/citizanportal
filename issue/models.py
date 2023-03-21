from django.db import models

from django.contrib.auth.models import User

class Issue(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    issue=models.TextField()
    description=models.TextField(blank=True,null=True)
    location=models.TextField()
    image=models.ImageField(upload_to='issue/',blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.issue