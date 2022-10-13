from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

# def home(request):
#     return HttpResponse("Hello Home page!!")

def home(request):
    return render(request, 'index.html')
def courses(request):
    return render(request, 'courses.html')
def course_single(request):
    return render(request, 'course-single.html')
def teachers(request):
    return render(request, 'teachers.html')
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
