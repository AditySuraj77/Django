from django.shortcuts import render,redirect
from album.models import Songlist
from django.contrib import messages
from datetime import datetime
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('song_name')
            genre = request.POST.get('song_genre')
            artist = request.POST.get('song_artist')
            date = request.POST.get('song_date')
            img = request.FILES.get('song_img')
            audio = request.FILES.get('song_audio')
            print(name,genre,artist,date,img,audio)

        except Exception as e:
            print(e)
        else:
            song = Songlist(
                name=name,
                genre=genre,
                artists=artist,
                date=date,
                img=img,
                audio=audio
            )
            song.save()
            messages.success(request,'Item Added Sucessfully ! ', )
            return redirect(home)



    return render(request,'home.html')


def list_of_songs(request):
    song_lst = Songlist.objects.all()

    pagenator = Paginator(song_lst,2)
    page_num = request.GET.get('page')
    page_services = pagenator.get_page(page_num)
    total_page = page_services.paginator.num_pages
    data = {'data':page_services,
            'lastpage':total_page,
            'totalpagelist':[n+1 for n in range(total_page)]}  # Code For Pagination
    return render(request,'songlist.html',data)


@login_required(login_url='/login/')
def delete_item(request,del_id):
    del_item = Songlist.objects.get(id=del_id)
    del_item.delete()
    messages.info(request,'Selected Item was Deleted')
    return redirect(list_of_songs)

@login_required(login_url='/login/')
def update_item(request,updt_id):
    display_item = Songlist.objects.get(id=updt_id)
    if request.method == 'POST':
        try:
            name = request.POST.get('song_name')
            genre = request.POST.get('song_genre')
            artist = request.POST.get('song_artist')
            date = request.POST.get('song_date')
            img = request.FILES.get('song_img')
            audio = request.FILES.get('song_audio')
            print(name, genre, artist, date, img, audio)
        except Exception as e:
            print(e)
        else:
            display_item.name = name
            display_item.genre = genre
            display_item.artists = artist
            if img != None:
                display_item.img = img
                if audio != None:
                    display_item.audio = audio
                else:
                    display_item.audio = display_item.audio
            else:
                display_item.img = display_item.img

            display_item.save()
            messages.success(request,'Item Updated')
            return redirect(list_of_songs)



    return render(request,'update.html',{'data':display_item})

def contact(request):
    return render(request,'contact.html')


#     ~~~~~~~~~~~~~~~~~~~~~~~Authentication~~~~~~~~~~~~~~~~~~~~~~~

def Register_page(request):
    if request.method == "POST":
            fullname = request.POST.get('fullname')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already exists Choose Another UserName')
                return redirect(Register_page)


            user = User.objects.create(
                first_name=fullname,
                username=username,
                email=email
            )
            user.set_password(password)
            user.save()
            messages.success(request,'Account Created Successfully')
            return redirect(Register_page)
    return render(request,'register.html')

def login_page(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            if not User.objects.filter(username=username).exists():
                messages.info(request,'username Does not exists Please SignIn')
                return redirect(login_page)

            user = authenticate(username=username, password=password)
            if user is None:
                messages.info(request, 'Incorrect Password')
                return redirect(login_page)

            else:
                login(request, user)
                messages.success(request, 'You are login now')




            return redirect(home)




    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return render(request,'login.html')
