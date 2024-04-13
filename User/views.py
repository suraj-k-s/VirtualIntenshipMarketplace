from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
# Create your views here.

def homepage(request):
    user = tbl_User.objects.get(id=request.session['uid'])
    return render(request,"User/HomePage.html",{"user":user})

def myprofile(request):
    user = tbl_User.objects.get(id=request.session['uid'])
    return render(request,"User/Myprofile.html",{"user":user})

def editprofile(request):
    user=tbl_User.objects.get(id=request.session['uid'])
    if request.method=="POST":
        print("hai")
        user.user_name=request.POST.get("text_name")
        user.user_contact=request.POST.get("text_contact")
        user.user_address=request.POST.get("text_address")
        user.user_bio=request.POST.get("text_bio")
        user.save()
        return redirect("webuser:homepage")
    else:
        return render(request,"User/EditProfile.html",{"user":user})
    

def CPUser(request):
    if request.method=="POST":
        user=tbl_User.objects.get(id=request.session['uid'])
        opassword=request.POST.get("txt_opassword")
        npassword=request.POST.get("txt_npassword")
        cpassword=request.POST.get("txt_cpassword")
        if user.user_password==opassword:
            if npassword == cpassword:
                user.user_password=request.POST.get("txt_npassword")
                user.save()
                return redirect("webuser:homepage")
            else:
                msg="password missmatch !"
                return render(request,"User/Changepassword.html",{'msg':msg})
        else:
            msg="password missmatch !"
            return render(request,"User/Changepassword.html",{'msg':msg})
    else:
        return render(request,"User/Changepassword.html")
    


