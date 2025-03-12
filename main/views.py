from django.shortcuts import render,redirect,get_object_or_404
from .models import Users,Family
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    newusers=Users.objects.all().values()
    context={
        'newusers':newusers,
    }
    return render(request,'index.html',context)

def detail(request,id):

    users=Users.objects.get(id=id)  
    families=users.child_of_families.first()
    
    context={
        'user':users,
        "family":families
    }
    return render(request,'detail.html',context)

@login_required
def home(request):
    return render(request,'home.html')


def family(request):
    family=Family.objects.all().values()
    context={
        'family':family
    }
    return render(request,'family.html',context)

def family_detail(request,id):
    family=Family.objects.get(id=id)
    context={
        'family':family,
    }
    return render(request,'family_detail.html',context)

def signUpView(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})


def createUser(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=UserForm()
    return render(request,'createuser.html',{'form':form})

def createFamily(request):
    if request.method=='POST':
        form=FamilyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=FamilyForm()
    return render(request,'createfamily.html',{'form':form})

def update_family(request,id):
    # family=Family.objects.all(id=id)
    famillies = get_object_or_404(Family, id=id) 
    form=FamilyForm(instance=famillies)
    if request.method=='POST':
        form=FamilyForm(request.POST,instance=famillies)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'update_details.html',context)

def delete_family(request,id):
    data=get_object_or_404(Family, id=id) 
    if request.method=='POST':
        data.delete()
        return redirect("/")
    return render(request,'delete.html',{'obj':data})


def update_user(request,id):
    # family=Family.objects.all(id=id)
    user = get_object_or_404(Users, id=id) 
    form=UserForm(instance=user)
    if request.method=='POST':
        form=UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'update_details.html',context)

def delete_user(request,id):
    data=get_object_or_404(Users.all_objects, id=id) 
    if request.method=='POST':
        data.soft_delete()
        return redirect("/")
    return render(request,'delete.html',{'obj':data})


# def tree(request,id):
#     families=get_object_or_404(Family, id=id) 
#     context={
#         'families':families
#     }
    
#     return render(request,'tree.html',context)

def tree(request,id):
    father_family=None
    mother_family=None
    users=Users.objects.get(id=id)
    family=Family.objects.filter(child=users).first()
    # families=users.child_of_families.first()
    if family and family.father:
        father_family=family.father.child_of_families.first()
    if family and family.mother:
        mother_family=family.mother.child_of_families.first()
    context={
        'users':users,
        'family':family,
        'father_family':father_family,
        "mother_family": mother_family
    }
    return render(request,'tree.html',context)

# def tree(request,id):
    
#     family=Family.objects.filter(id=id)
#     father_name=family.father.__str__ if family.father else "Unknown"
#     mother_name=family.mother.__str__ if family.mother else "Unknown"
    
#     context={
#         "family": family,
#         "father_name": father_name,
#         "mother_name": mother_name
#     }
#     return render(request,'tree.html',context)\





