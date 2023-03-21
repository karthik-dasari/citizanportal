from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Violation

@login_required(login_url='auth:login')
def home(request):
    return render(request, 'violation/home.html')

@login_required(login_url='auth:login')
def submit(request):
    if request.method == 'POST':
        description = request.POST.get('description','')
        location = request.POST.get('location','')
        image = request.FILES.get('image','')
        if image is not None:
            Violation.objects.create(user_id=request.user.id, description=description, location=location, image=image)
        else:
            Violation.objects.create(user_id=request.user.id, description=description, location=location)
        return redirect('auth:home')