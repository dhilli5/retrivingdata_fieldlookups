from django.shortcuts import render

from django.db.models.functions import Length

# Create your views here.


from app.models import *

def display_course(request):
    LOC=Course.objects.all()
    d={'course':LOC}
    
    return render(request,"display_course.html",context=d)

def display_student(request):
    LOS=Student.objects.all()
    #LOS=Student.objects.filter(mno__gte=898594557)
    #LOS=Student.objects.order_by(Length('mno'))    (this case data will arrange the ascending order)
    
    #LOS=Student.objects.exclude(mno=9985077649)     (this case get the data except,to given in the exclude method)
    d1={'student':LOS}
    
    return render(request,"display_student.html",context=d1)
def display_address(request):
    LOA=Address.objects.all()
    #LOA=Address.objects.all()[:2:]   (this case you can access the particular value)
    #LOA=Address.objects.order_by('st_name')    (in this case to get the ascending order)
    #LOA=Address.objects.order_by('-st_name')   (in this case to get the data in descending order)
    
    #LOA=Address.objects.order_by(Length('st_name').desc())
    
    
    
    d2={'address':LOA}
    
    return render(request,"display_address.html",context=d2)

def display_all(request):
    LOC=Course.objects.all()
    LOS=Student.objects.all()
    LOA=Address.objects.all()
    d={'course':LOC,'student':LOS,'address':LOA}
    return render(request,"display_all.html",context=d)
    