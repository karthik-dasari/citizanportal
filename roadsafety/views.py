from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from roadsafety.models import RoadSafety

@login_required(login_url='auth:login')
def home(request):
    return render(request, 'roadsafety/home.html')

@login_required(login_url='auth:login')
def submit(request):
    if request.method == 'POST':
        user=User.objects.filter(id=request.user.id).first()
        problem = request.POST.get('problem','')
        description = request.POST.get('description','')
        location = request.POST.get('location','')
        image = request.FILES.get('image','')
        if image is not None:
            RoadSafety.objects.create(user_id=request.user.id, problem=problem, description=description, location=location, image=image)
        else:
            RoadSafety.objects.create(user_id=request.user.id, problem=problem, description=description, location=location)
        return redirect('auth:home')