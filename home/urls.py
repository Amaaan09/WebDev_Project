from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    
    path("courses/", views.courses, name="courses"),
    
    path("courses_after_login/", views.courses_after_login, name="courses_after_login"),
    path("courses_single/<str:hm>/", views.course_single, name="course-single"),
    path("courses_add/", views.courses_add, name="courses_add"),
    path("courses_delete/<str:id>/", views.courses_delete, name="courses_delete"),
    
    
    path("teachers/", views.teachers, name="teachers"),
    path("events/", views.events, name="events"),
    path("aboutUs/", views.aboutUs, name="aboutUs"),
    path("contact/", views.contact, name="contact"),
    path("news/", views.news, name="news"),
    path("gallery/", views.gallery, name="gallery"),
    
]