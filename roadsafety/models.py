from django.db import models
from django.contrib.auth.models import User

class RoadSafety(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    problem=models.TextField()
    description=models.TextField(blank=True,null=True)
    location=models.TextField()
    image=models.ImageField(upload_to='roadsafety/',blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.problem