from django.shortcuts import render, redirect
from todo.models import User


def home(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')

        user = User(fname=fname, lname=lname, email=email)
        user.save()
        message = 'Form Submitted Sucessfully !'
        return render(request, 'home.html', {'message': message})

    return render(request, 'home.html')


def detail(request):
    user = User.objects.all()
    data = {'data': user}

    return render(request, 'detail.html', data)


def delete(request, num_id):
    user = User.objects.get(id=num_id)
    user.delete()
    return redirect(detail)


def edit(request, edit_id):
    user = User.objects.get(id=edit_id)
    data = {'d': user}
    return render(request, 'edit.html', data)


def updaterecord(request, update_id):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    update_user = User.objects.get(id=update_id)
    update_user.fname = fname
    update_user.lname = lname
    update_user.email = email
    update_user.save()
    return redirect(detail)
