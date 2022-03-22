from django.shortcuts import  render,HttpResponseRedirect
from .forms import studentRegistration
from .models import User

# Create your views here.
def addshow(request):
      if request.method == 'POST':
            fm = studentRegistration(request.POST)
            if fm.is_valid():
                  nm = fm.cleaned_data['name']
                  em =fm.cleaned_data['email']
                  pas = fm.cleaned_data['password']
                  reg =User(name=nm, email=em,password=pas)
                  reg.save()
                  fm = studentRegistration()
      else:
            fm = studentRegistration()
      student = User.objects.all()

      return render(request, 'enroll/addandshow.html',{'form':fm, 'student':student})

def update_data(request, id):
      if request.method == 'POST':
            user =User.objects.get(pk =id)
            fm = studentRegistration(request.POST,instance=user)
            if fm.is_valid():
                  fm.save()
            return HttpResponseRedirect('/')
      else:
            user =User.objects.get(pk=id)
            fm =studentRegistration(instance=user)

      return render(request,'enroll/update.html',{'form':fm})


def delete_data(request,id):
      if request.method == 'POST':
            user =User.objects.get(pk=id)
            user.delete()
      
      return HttpResponseRedirect('/')