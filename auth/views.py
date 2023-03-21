from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

from geopy.geocoders import Nominatim
from accident.models import Accident
from roadsafety.models import RoadSafety
from issue.models import Issue
from violation.models import Violation

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.email =="hospital@gmail.com":
                return redirect('policedashboard')
            return redirect('home')
        else:
            return render(request, 'auth/login.html')
    else:
        if request.user.is_authenticated:
            return redirect('auth:home')
        else:
            return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname','')
        lname = request.POST.get('lname','')
        password = request.POST.get('password','')
        email = request.POST.get('email','')
        try:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=fname, last_name=lname)
            auth_login(request, user)
        except:
            return render(request, 'auth/register.html')
        return redirect('auth:home')
    else:
        return render(request, 'auth/register.html')

def logout(request):
    auth_logout(request)
    return redirect('auth:login')

@login_required(login_url='auth:login')
def home(request):
    return render(request, 'auth/home.html')

@login_required(login_url='auth:login')
def category(request):
    if request.method == 'POST':
        category = request.POST.get('category','')
        if category == "road safety":
            return redirect('roadsafety:home')
        elif category == "report violation":
            return redirect('violation:home')
        elif category == "report accident":
            return redirect('accident:home')
        elif category == "raise an issue":
            return redirect('issue:home')

def getlocation(request):
    if request.method == 'POST':
        latitude = request.POST.get('lat','')
        longitude = request.POST.get('lng','')
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.reverse(latitude+","+longitude)
        return JsonResponse({'location': str(location)})

@login_required(login_url='auth:login')
def dashboard(request):
    data=[]
    issues = Issue.objects.filter(user_id=request.user.id)
    violations = Violation.objects.filter(user_id=request.user.id)
    accidents = Accident.objects.filter(user_id=request.user.id)
    road_safety = RoadSafety.objects.filter(user_id=request.user.id)
    for i in issues:
        dic={'title': i.issue, 'category': 'issue','location': i.location, 'date': i.date, 'description': i.description, 'image': None}
        if i.image:
            dic['image']=i.image
        data.append(dic)
    for i in violations:
        dic={'title': None, 'category': 'violation','location': i.location, 'date': i.date, 'description': i.description, 'image': None}
        if i.image:
            dic['image']=i.image
        data.append(dic)
    for i in accidents:
        dic={'title': None, 'category': 'accident','location': i.location, 'date': i.date, 'description': i.description, 'image': None}
        if i.image:
            dic['image']=i.image
        data.append(dic)
    for i in road_safety:
        dic={'title': i.problem, 'category': 'road safety','location': i.location, 'date': i.date, 'description': None, 'image': None}
        if i.image:
            dic['image']=i.image
        if i.description:
            dic['description']=i.description
        data.append(dic)
    return render(request, 'auth/dashboard.html', {'data': data})

@login_required(login_url='auth:login')
def policedashboard(request):
    data=[]
    issues = Issue.objects.all()
    violations = Violation.objects.all()
    accidents = Accident.objects.all()
    road_safety = RoadSafety.objects.all()
    for i in issues:
        dic={'title': i.issue, 'category': 'issue','location': i.location, 'date': i.date, 'description': i.description, 'image': None}
        if i.image:
            dic['image']=i.image
        data.append(dic)
    for i in violations:
        dic={'title': None, 'category': 'violation','location': i.location, 'date': i.date, 'description': i.description, 'image': None}
        if i.image:
            dic['image']=i.image
        data.append(dic)
    for i in accidents:
        dic={'title': None, 'category': 'accident','location': i.location, 'date': i.date, 'description': i.description, 'image': None}
        if i.image:
            dic['image']=i.image
        data.append(dic)
    for i in road_safety:
        dic={'title': i.problem, 'category': 'road safety','location': i.location, 'date': i.date, 'description': None, 'image': None}
        if i.image:
            dic['image']=i.image
        if i.description:
            dic['description']=i.description
        data.append(dic)
    return render(request, 'policedashboard.html', {'data': data})