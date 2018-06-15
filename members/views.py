from django.shortcuts import render
from .models import Member

def member(request):
    all_mmeber=Mmeber.objects.all()
    context={'Mmeber':Member}
    return render(request,'members/memberpage.html',context)
