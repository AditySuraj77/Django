from django.shortcuts import render

from .forms import EditorForm

def home(request):



    form = EditorForm()
    return render(request,'index.html',{'form':form})

# Create your views here.
