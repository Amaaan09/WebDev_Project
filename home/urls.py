from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    
    path("courses/", views.courses, name="courses"),
    path("courses_single/", views.course_single, name="course-single"),
    path("teachers/", views.teachers, name="teachers"),
    path("events/", views.events, name="events"),
    path("aboutUs/", views.aboutUs, name="aboutUs"),
    path("contact/", views.contact, name="contact"),
    path("news/", views.news, name="news"),
    path("gallery/", views.gallery, name="gallery"),
    path("login/", views.login_page, name="login_page")
]