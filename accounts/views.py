from re import I
from django.shortcuts import render,redirect,reverse
from.forms import Signupform,Profilemodel,Usermodel
from django.contrib.auth import authenticate,login
from django.urls.base import reverse
from.models import Profile
# Create your views here.
def profile(request):
    profil=Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profil})


def profile_edit(request):
    userprofile = Profile.objects.get(user=request.user)
    print('123456')
    print(userprofile)
    print('123456')
    if request.method=='POST':
             userform=Usermodel(request.POST,instance=request.user)
             profilefor=Profilemodel(request.POST,request.FILES,instance=userprofile)
             if userform.is_valid() and profilefor.is_valid():
                print('10101010')
                userform.save()
                myprofile= profilefor.save(commit=False)
                myprofile.user=request.user
                myprofile.save()
                return redirect(reverse('accounts:profile'))


    else :
        userform=Usermodel(instance=request.user)
        profilefor=Profilemodel(instance=userprofile)
 

    return render(request,'accounts/profile_edit.html',{'userform':userform,'profileform':profilefor})



def signup(request):
    if request.method=="POST":
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = Signupform()
    return render(request,'registration/signup.html',{'form':form})
