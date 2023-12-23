from django.shortcuts import render
from shop.models import Category,Product
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def allcategories(request):
    c = Category.objects.all()
    return render(request,'category.html',{'c':c})

def allproducts(request,p):
    c=Category.objects.get(name=p)
    p=Product.objects.filter(category=c)
    return render(request,'product.html',{'c':c,'p':p})
def alldetails(request,p):
    n = Product.objects.get(name=p)
    return render(request,'details.html',{'n':n})

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        e=request.POST['e']
        if(p==cp):
            user=User.objects.create_user(username=u,password=p,email=e)
            user.save()
            return allcategories(request)
        else:
            return HttpResponse("password not matching")
    return render(request,'register.html')
def user_login(request):
    if (request.method == "POST"):
        name=request.POST['u']
        passw=request.POST['p']
        user=authenticate(username=name,password=passw)
        if user:
            login(request,user)
            return allcategories(request)
        else:
            messages.error(request,'Invalid Credentails')

    return render(request,'login.html')
@login_required
def user_logout(request):
    logout(request)
    return user_login(request)







