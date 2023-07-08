from django.shortcuts import render,redirect
from . models import TaskDB
from . forms import TaskForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = TaskDB.objects.all()
            messages.success(request,('New item added!!'))
            return render(request,'index.html',{'all_items':all_items})
        
    else:
        all_items = TaskDB.objects.all()
        return render(request,'index.html',{'all_items':all_items})

def delete(request,list_id):
    item = TaskDB.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('Item has been deleted!!'))
    return redirect('home') #refreshes the page