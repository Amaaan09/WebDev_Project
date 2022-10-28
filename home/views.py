from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm
# Create your views here.



def home(request):
    return render(request, 'index.html')

def courses(request):
    return render(request, 'courses.html')

@login_required(login_url="login_page")
def courses_after_login(request):
    try:
        data = Course.objects.all()
        context = {"course":data}
    except Exception as e:
        context = {"course":"data not found"}
    return render(request, 'courses_after_login.html', context)

# @login_required(login_url="login_page")
def course_single(request, id):
    fetch_data = Course.objects.get(id=id)
    context = {"fetch_data":fetch_data}
    return render(request, 'course-single.html', context)

def courses_add(request):
    form = CourseForm()
    if request.method == 'POST':
        myData = CourseForm(request.POST)
        if myData.is_valid():
            myData.save()
            return redirect('courses_after_login')
    context = {"form":form}
    return render(request, 'courses_add.html', context)

def courses_delete(request, id):
    data = Course.objects.get(id=id)
    data.delete()
    return redirect('courses_after_login')
    

@login_required(login_url="login_page")
# @permission_required('', login_url="home")
def teachers(request):
    return render(request, 'teachers.html')

@login_required(login_url="login_page")
def events(request):
    return render(request, 'events.html')

def aboutUs(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def news(request):
    return render(request, 'news.html')
def gallery(request):
    return render(request, "gallery.html")
