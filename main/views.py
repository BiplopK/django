from django.shortcuts import render
from .models import User
from django.template import loader
# Create your views here.
def index(request):
    newusers=User.objects.all().values()
    context={
        'newusers':newusers,
    }
    return render(request,'index.html',context)

def detail(request,id):
    users=User.objects.get(id=id)
    context={
        'user':users,
    }
    return render(request,'detail.html',context)

def home(request):
    return render(request,'home.html')