from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Issue

@login_required(login_url='auth:login')
def home(request):
    return render(request, 'issue/home.html')

@login_required(login_url='auth:login')
def submit(request):
    if request.method == 'POST':
        issue = request.POST.get('problem','')
        description = request.POST.get('description','')
        location = request.POST.get('location','')
        image = request.FILES.get('image','')
        if image is not None:
            Issue.objects.create(user_id=request.user.id, issue=issue, description=description, location=location, image=image)
        else:
            Issue.objects.create(user_id=request.user.id, issue=issue, description=description, location=location)
        return redirect('auth:home')