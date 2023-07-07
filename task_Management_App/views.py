from django.shortcuts import render
from . models import TaskDB

# Create your views here.
def home(request):
    all_items = TaskDB.objects.all()
    return render(request,'index.html',{'all_items':all_items})
