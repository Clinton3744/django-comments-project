from django.shortcuts import render,redirect
from commandapp.models import Details
from commandapp.forms import DetailsForm
import datetime


def retrive_commend(request):

    data=Details.objects.all()
    form=DetailsForm()
    time=datetime.datetime.now()
    
    if request.method=='POST':

        form=DetailsForm(request.POST)

        if form.is_valid():

            form.save()

    return render(request,'commandapp/index.html',context={'data':data,'form':form,'time':time})


def delete_commend(request,id):

    data=Details.objects.get(id=id)

    data.delete()

    return redirect('/commandapp')

