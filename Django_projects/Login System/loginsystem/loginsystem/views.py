from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.admin import User
from django.contrib import messages


#@login_required(login_url='/signin/')
def home(request):
    return render(request,'home.html')


def signUp_page(request):
    if request.method == 'POST':
        try:
            fname = request.POST['fname']
            lname = request.POST['lname']
            username = request.POST['username']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            print(fname,lname,username,email,pass1,pass2)
        except Exception as e:
            print(e)
        else:

            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Already Taken Try Another Username !')
                return redirect(signUp_page)
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email Already Taken Try Another Email !')
                return redirect(signUp_page)

            if len(username)>10:
                messages.error(request,'Length of username is not valid ! ')
                return redirect(signUp_page)
            if pass1 != pass2:
                messages.error(request,"Password Does't not Match !")
                return redirect(signUp_page)

            myuser = User.objects.create(
                first_name = fname,
                last_name = lname,
                username = username,
                email = email,

            )
            myuser.set_password(pass2)
            myuser.save()
            messages.success(request,f'Welcome {username} Your Account Created Sucessfully')
            return redirect(signUp_page)



    return render(request,'signup.html')

def signIn_page(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['pass']
        except Exception as e:
            print(e)

        else:
            if not User.objects.filter(username=username).exists():
                messages.error(request,'Username Not Exists Please SignIn !')
                return redirect(signIn_page)
            myuser = authenticate(username=username,password=password)

            if myuser is None:
                messages.error(request,'Password Invalid !')
                return redirect(signIn_page)
            else:
                login(request,myuser)
                messages.success(request,f'{username} You are SignIn Now')
                return redirect(home)
    return render(request,'signIn.html')


def signout(request):
    logout(request)
    messages.success(request,'SignOut Sucessful')
    return render(request,'home.html')