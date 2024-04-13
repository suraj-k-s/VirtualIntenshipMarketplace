from django.shortcuts import render

# Create your views here.
def calculation(request):
    result=""
    if request.method=="POST":
        no1=int(request.POST.get('txtno1'))
        no2=int(request.POST.get('txtno2'))
        no2=int(request.POST.get('txtno3'))
        btn=request.POST.get('btnsubmit')
        if btn=="+":
            result=no1+no2
        elif btn=="-":
            result=no1-no2
        elif btn=="X":
            result=no1*no2
        elif btn=="/":
            result=no1/no2
        return render(request,"Basics/Calculator.html",{'res':result})
    else:
        return render(request,"Basics/Calculator.html",{'res':result})
    
def largesmall(request):
    largest=""
    smallest=""
    if request.method=="POST":
        no1=int(request.POST.get('txtno1'))
        no2=int(request.POST.get('txtno2'))
        no3=int(request.POST.get('txtno3'))
        btn=request.POST.get('btnsubmit')
        if btn=="Submit":
            if((no1>no2)and(no1>no3)):
                largest = no1
            elif((no2>no1)and(no2>no3)):
                largest=no2
            else:
                largest=no3
            if((no1<no2)and(no1<no3)):
                smallest = no1
            elif((no2<no1)and(no2<no3)):
                smallest=no2
            else:
                smallest=no3
            return render(request,"Basics/LargestSmallest.html",{'large':largest,'small':smallest})
    else:
        return render(request,"Basics/LargestSmallest.html",{'large':largest,'small':smallest})
    


    
    




      
