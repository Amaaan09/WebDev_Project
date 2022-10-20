from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
# Create your views here.



def home(request):
    return render(request, 'index.html')

@login_required(login_url="login_page")
def courses(request):
    return render(request, 'courses.html')

@login_required(login_url="login_page")
def course_single(request):
    return render(request, 'course-single.html')

@login_required(login_url="login_page")
# @permission_required('', login_url="home")
def teachers(request):
    return render(request, 'teachers.html')

# @login_required(login_url="login_page")
def events(request):
    return render(request, 'events_crud/eventsLand.html')

def aboutUs(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def news(request):
    return render(request, 'news.html')
def gallery(request):
    return render(request, "gallery.html")
