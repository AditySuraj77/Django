from django.shortcuts import render,redirect
#from django.http import HttpResponse
from todo.models import ToDo
def home(request):
    return render(request,'home.html')

def add(request):
    if request.method == 'POST':
        try:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
        except:
            print(UserWarning)
        else:
            to_do = ToDo(fname=fname,lname=lname,email=email,phone=phone)
            to_do.save()
            return redirect(details)

    return render(request,'add.html')

def details(request):
    user = ToDo.objects.all()
    data = {'data':user}

    return render(request,'detail.html',data)

def delete(request,del_id):
    user = ToDo.objects.get(id=del_id)
    user.delete()
    return redirect(details)

def edit(request,edit_id):
    user = ToDo.objects.get(id=edit_id)
    data = {'data':user}
    return render(request,'update.html',data)

def update(request,update_id):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        user = ToDo.objects.get(id=update_id)

        user.fname = fname
        user.lname = lname
        user.email = email
        user.phone = phone

        user.save()
        return redirect(details)

    return render(request,'update.html')