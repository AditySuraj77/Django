from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'logreg.html')



def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request,'Username Not Exists !')
            return redirect(login_page)

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request,'Invalid Password')
            return redirect(login_page)
        else:
            login(request,user)
            return redirect(dashboard)
    return render(request,'login.html')


def logout_page(request):
    logout(request)
    return redirect(home)
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username Already Exist Provide Unique UserName')
            return redirect(register)

        user = User.objects.create(
            first_name = first_name,
            username = username,
            password = password
        )

        user.set_password(password)
        user.save()
        messages.success(request,'Account Created Sucessfully !')
    return render(request,'register.html')



@login_required(login_url='/login')
def dashboard(requset):
    return render(requset,'dashboard.html')


@login_required(login_url='/login')
def about(request):
    return render(request,'about.html')