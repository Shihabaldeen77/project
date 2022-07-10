import imp
from django.shortcuts import render
from.models import Info
# Create your views here.
def Contact(request):
    myinfo=Info.objects.first()

    return render(request,'contact/contact.html',{'myinfo':myinfo})