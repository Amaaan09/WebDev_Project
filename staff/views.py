from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from django.contrib import messages

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            print("credentials are incorrect.")
            return redirect("signup_page")
    return render(request, "login_page.html")

def signup_page(request):  
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request, "signup_page.html", context={"register_form":form})

def logout_page(request):
    print("logout")
    logout(request)
    return redirect("home")