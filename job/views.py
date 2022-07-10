import imp
from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from.form import Applayform,Addjob
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import Jopfilter
# Create your views here.

def Joblist(request):
    joblist=Job.objects.all()
    nummper=Job.objects.count()

    print('+++++++++++++++++++++++++++++++++')

    print('+++++++++++++++++++++++++++++++++')
    myfilte=Jopfilter(request.GET,queryset=joblist)
    joblist=myfilte.qs
    paginator=Paginator(joblist,4)
    pagenumper=request.GET.get('page')
    pageobject=paginator.get_page(pagenumper)

    contects={'jobs':pageobject,'myfilter':myfilte,'nummper':nummper}
    return render(request,'job/job_list.html',contects)

def jobdetails(request,slug):
    jopp=Job.objects.get(slug=slug)
    print('=================')
    print(jopp)
    print('=================')
    if request.method=='POST':
        form=Applayform(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=jopp
            myform.save()
    else:
         form=Applayform()

    joppd={"job":jopp,'form':form}
    return render(request,'job/job_detail.html',joppd)

@login_required
def add_job(request):
     if request.method=='POST':
        form=Addjob(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            return redirect (reverse('jobs:job_listt'))
     else:
         form=Addjob()
    
     return render(request,'job/add_job.html',{'form':form})
 

 