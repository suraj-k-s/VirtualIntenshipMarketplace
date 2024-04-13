from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.
def Home(request):
   return render(request,"Guest/Homepage.html")
    
def Company_Insert_Select(request):
    district=tbl_district.objects.all()
    if request.method == "POST":
       # dis = tbl_district.objects.get(id=request.POST.get("district"))
        #tbl_Company.objects.create(company_photo=request.FILES.get("photo"))
        return render(request,"Guest/Company.html",{"district_id":district})
    else:
        return render(request,"Guest/Company.html",{"district_id":district})
    
#def User_Insert_Select(request):
    district=tbl_district.objects.all()
    if request.method == "POST":
        # dis = tbl_district.objects.get(id=request.POST.get("district"))
        tbl_User.objects.create(user_photo=request.FILES.get("photo"))
        return render(request,"Guest/User.html",{"district_id":district})
    else:
        return render(request,"Guest/User.html",{"district_id":district})
    
def Place_Insert_Select(request):
    Placedata=tbl_Place.objects.all()
    district = tbl_district.objects.all()
    if request.method == "POST":
        dis = tbl_district.objects.get(id=request.POST.get("district"))
        tbl_Place.objects.create(Place_name=request.POST.get("PlaceName"),district=dis)
        return render(request,"Admin/Place.html",{"data":Placedata,"districtdata":district})
    else:
        return render(request,"Admin/place.html",{"data":Placedata,"districtdata":district})
    






def User_Insert_Select(request):
    dis=tbl_district.objects.all()
    if request.method=="POST" and request.FILES:
        tbl_User.objects.create(
            user_name=request.POST.get('name'),
            user_contact=request.POST.get('contact'),
            user_email=request.POST.get('email'),
            user_address=request.POST.get('details'),
            place_id=request.POST.get('sel_place'),
            user_proof=request.FILES.get('proof'),
            user_photo=request.FILES.get('photo'),
            user_password=request.POST.get('password')
        )
        return render(request,'Guest/User.html',{'district_id':dis})
    else:
        return render(request,'Guest/User.html',{'district_id':dis})

def Company_Insert_Select(request):
    dis=tbl_district.objects.all()
    if request.method=="POST" and request.FILES:
        placedata = tbl_Place.objects.get(id=request.POST.get('place'))
        tbl_Company.objects.create(
            company_name=request.POST.get('name'),
            company_contact=request.POST.get('contact'),
            company_email=request.POST.get('email'),
            company_address=request.POST.get('details'),
            place=placedata,
            company_proof=request.FILES.get('proof'),
            company_photo=request.FILES.get('photo'),
            company_password=request.POST.get('password')
        )
        return render(request,'Guest/Company.html',{'district_id':dis})
    else:
        return render(request,'Guest/Company.html',{'district_id':dis})

    
def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_Place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{"place":place})


def Login_Insert_Select(request):
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            usercount = tbl_User.objects.filter(user_email=email,user_password=password).count()
            print(usercount)
            companycount = tbl_Company.objects.filter(company_email=email,company_password=password).count()
            if usercount > 0:
                user = tbl_User.objects.get(user_email=email,user_password=password)
                request.session["uid"] = user.id
                return redirect("webuser:homepage")
            elif companycount > 0:
                company = tbl_Company.objects.get(company_email=email,company_password=password)
                request.session["cid"] = company.id
            
                return redirect("webcompany:homepage")
            else:
                return render(request,"Guest/Login.html")
        else:
            return render(request,"Guest/Login.html")
        

