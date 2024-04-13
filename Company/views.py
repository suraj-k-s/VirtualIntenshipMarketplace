from django.shortcuts import render,redirect
from Company.models import *
from Guest.models import *
# Create your views here.
#def Changepassword_Insert_Select(request):
 #   if request.method == "POST":
  #      tbl_Changepassword.objects.create(Changepassword_name=request.POST.get("Changepassword_name"))
   #     return render(request,"Company/Changepassword.html")
    #else:
     #   return render(request,"Company/Changepassword.html")
    
def homepage(request):
    company = tbl_Company.objects.get(id=request.session['cid'])
    return render(request,"Company/Homepage.html")

def myprofile(request):
    company = tbl_Company.objects.get(id=request.session['cid'])
    return render(request,"Company/Myprofile.html",{"company":company})

def Intenship_Insert_Select(request):
    dis=tbl_Intenship.objects.all()
    cdata=tbl_Company.objects.get(id=request.session['cid'])
    if request.method=="POST" and request.FILES:
        tbl_Intenship.objects.create(
          Intenship_duration=request.POST.get('duration'),
           Intenship_details=request.POST.get('details'),
           Intenship_poster=request.FILES.get('poster'),
           Company = cdata
        )
        return render(request,'Company/Intenship.html',{'Intenship_id':dis})
    else:
        return render(request,'Company/Intenship.html',{'Intenship_id':dis})
    

    