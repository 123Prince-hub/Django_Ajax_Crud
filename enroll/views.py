from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import StudentRegistration
from django.views.decorators.csrf import csrf_exempt
from .models import Curd

# Create your views here.
def home(request):
    fm = StudentRegistration()
    stud = Curd.objects.all()
    return render(request, 'index.html', {'form':fm, 'std':stud})


@csrf_exempt
def saveData(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            usr = Curd(name=name, email=email, password=password)
            usr.save()
            return JsonResponse({'status':'Save'})
        else:
            return JsonResponse({'status':'Fail'})