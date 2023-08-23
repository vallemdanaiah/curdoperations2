from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def Home(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        form.save()
        form=StudentForm()
        return redirect('register')
    
    data=Student.objects.all()    
           
    context={
        'form':form,
        'data':data,
    }
    return render(request,'index.html',context)

 #register_form
def Register(request):
    std=Student.objects.all()
    # std.Register()
    if request.method=='POST':
        std=Student.objects.all()
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('register')
        
    else:
        std=Student.objects.all()
        form=StudentForm()
    context={
        'form':form,
        'std':std,
    }
    return render (request,'register.html',context)
    
    
# Delete View
def Delete_record(request,id):
    a=Student.objects.get(pk=id)
    a.delete()
    return redirect('register')

#update View
def Update_record(request,id):
    if request.method=='POST':
        data=Student.objects.get(pk=id)
        form=StudentForm(request.POST,instance=data)
        if form.is_valid():
           form.save()
        return redirect('register')
    else:
        data=Student.objects.get(pk=id)
        form=StudentForm(instance=data)
    context={
        'form':form,
        'data':data,
    }
    return render (request,'update.html',context)
    

    
    
    