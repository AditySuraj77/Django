from django.shortcuts import render,redirect
from vegnonveg.models import Foods


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        img = request.FILES.get('img') # Save all data into database
        item = Foods(name=name,desc=desc,img=img)
        item.save()
        return redirect(home)


    food_item = Foods.objects.all()

    if request.GET.get('search'):
        print(request.GET.get('search'))
        food_item = food_item.filter(name__icontains=request.GET.get('search'))

    data = {'item': food_item}
    return render(request,'home.html',data)


def delete(request,del_id):
    item = Foods.objects.get(id=del_id)
    item.delete()
    return redirect(home)

def update(request,update_id):
    update_data = Foods.objects.get(id=update_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        img = request.FILES.get('img')

        update_data.name = name
        update_data.desc = desc
        if img != " ":
            update_data.img = img
        else:
            update_data.img = update_data.img
        update_data.save()
        return redirect(home)

    data = {'edit_data':update_data}
    return render(request,'edit.html',data)


