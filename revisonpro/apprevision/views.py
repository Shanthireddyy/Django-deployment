from django.shortcuts import render
# from django.http import HttpResponse
# from apprevision.models import User
from apprevision.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,'apprevision/index.html')

def users(request):
    # user_list=User.objects.order_by('first_name')
    # user_dict={'users':user_list}
    # return render(request,'apprevision/users.html',context=user_dict)

    form = NewUserForm()

    if request.method=="POST":
        form =NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)     #to return the home page index.html
        else:
            print("Form is Invalid")

    return render(request,'apprevision/users.html',{'form':form})




