from django.shortcuts import redirect, render,HttpResponse ,redirect
from .import models
from django.contrib.auth import authenticate,login,logout
import razorpay
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request,'home.html')

def ABOUT(request):
    return render(request,'about.html')

def menu(request):
    return render(request,'menu.html')
def links(request):
    return render(request,'links.html')

def donate(request):
    return render(request,'donate.html')

# ................................................................................................................
def parent(request):
    return render(request,'parent.html')


def insert(request):
    return render(request,'insert.html')
    
def save(request):
    if request.method == 'POST':
        name=request.POST['name']
        gender=request.POST['gender']
        nationality=request.POST['nationality']
        dateofbirth = request.POST['dateofbirth']
        occupation=request.POST['occupation']
        contact1 = request.POST['contact1']
        email=request.POST['email']
        Address = request.POST['Address']
        child_maintenance_amount = request.POST['child_maintenance_amount']
        motivation=request.POST['motivation']

        obj=models.parent()
        obj.name=name
        obj.gender=gender
        obj.nationality=nationality
        obj.dateofbirth=dateofbirth
        obj.occupation=occupation
        obj.Address=Address
        obj.child_maintenance_amount=child_maintenance_amount
        obj.contact1=contact1
        obj.email=email
        obj.motivation=motivation
        obj.save()
        print(name,gender,nationality,dateofbirth,occupation,Address,child_maintenance_amount,contact1,email,motivation,sep="/n")
    return redirect(show)

def show(request):
    objects=models.parent.objects.all()
    '''for obj in objects:
        print(obj.name,obj.gender,obj.nationality,obj.dateofbirth,obj.occupation,obj.address,obj.contact1,obj.email,obj.motivation,se="-")'''
    d={
        'title':' parent data page',
         'data': objects,

       }
    return render(request,'show.html',d)

def edit(request,id):
    obj = models.parent.objects.get(id=id)
    '''print(obj.id,obj.name,obj.mobile,obj.email,obj.address,sep='-')'''
    d={
        'title':' parent edit data',
        
        'data':obj,

    }
    return render(request,'edit.html',d)

def update(request):
    if request.method == 'POST':
        obj=models.parent()
        obj.id=request.POST['id']
        obj.name=request.POST['name']
        obj.gender=request.POST['gender']
        obj.nationality=request.POST['nationality']
        obj.dateofbirth=request.POST['dateofbirth']
        obj.occupation=request.POST['occupation']
        obj.Address=request.POST['Address']
        obj.child_maintenance_amount=request.POST['child_maintenance_amount']
        obj.contact1=request.POST['contact1']
        obj.email=request.POST['email']
        obj.motivation=request.POST['motivation']
        obj.save()
        return redirect(show)

def delete(request,id):
    rec=models.parent.objects.get(id=id)
    rec.delete()
    return redirect(show)
        
def childreg(request):
    return render(request,'childreg.html')

def childsave(request):
    if request.method =='POST':
        regno=request.POST['regno']
        orgname=request.POST['orgname']
        name=request.POST['name']
        gender=request.POST['gender']
        dateofbirth=request.POST['dateofbirth']
        fathername=request.POST['fathername']
        mothername=request.POST['mothername']
        address=request.POST['address']
    

        obj2=models.child()
        obj2.regno=regno
        obj2.orgname=orgname
        obj2.name=name
        obj2.gender=gender
        obj2.dateofbirth=dateofbirth
        obj2.fathername=fathername
        obj2.mothername=mothername
        obj2.address=address
        obj2.save()
        print(regno,orgname,name,gender,dateofbirth,fathername,mothername,address,sep="/n")

    return redirect(childshow)

def childshow(request):
    obj2=models.child.objects.all()
    '''for obj in objects:
        print(obj.name,obj.gender,obj.nationality,obj.dateofbirth,obj.occupation,obj.address,obj.contact,obj.email,obj.motivation,se="-")'''
    d={
        'title':' child data',
         'data': obj2,

    }
    return render(request,'childshow.html',d)
def childedit(request,id):
    obj2=models.child.objects.get(id=id)
    
    d={
        'title':'child edit page',
        'data':obj2,
    }
    return render(request,'childedit.html',d)

def updatechild(request):
    if request.method == 'POST':
        obj2=models.child()
        obj2.id=request.POST['id']
        obj2.regno=request.POST['regno']
        obj2.orgname=request.POST['orgname']
        obj2.name=request.POST['name']
        obj2.gender=request.POST['gender']
        obj2.dateofbirth=request.POST['dateofbirth']
        obj2.fathername=request.POST['fathername']
        obj2.mothername=request.POST['mothername']
        obj2.address=request.POST['address']
        obj2.save()
        return redirect(childshow)

def childdelete(request,id):
    recd=models.child.objects.get(id=id)
    recd.delete()
    return redirect(childshow)



def signin(request):
    return render(request,'login.html')


def loggin(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username ,password=password)
        if user !=None:
            login(request,user)
            return redirect(menu)
        else:
            return HttpResponse('login failed')    
    return HttpResponse('LOGIN FAILED')        


def loggout(request):
    logout(request)
    return redirect(home)


def abcd(request):
    '''
    child = models.child.objects.get(id=1)
    parent = models.parent.objects.get(id=1)
    obj = models.details()
    obj.child = child
    obj.parent = parent
    obj.save()
    '''
    return redirect(home)

def details(request):
    
    objs=models.details.objects.all()
    
    data={
        'title':'details page',
         'data': objs,

    }
    return render(request,'details.html',data)

def data(request,id):
    obj = models.details.objects.get(id = id)
    parent = models.parent.objects.get(id = obj.parent_id)
    child = models.child.objects.get(id = obj.child_id)
    d={
        'parent':parent,
        'child':child,
    }
    return render(request,'child_parent_details.html',d)