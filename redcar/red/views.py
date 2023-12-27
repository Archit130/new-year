from django.shortcuts import render, redirect
from red.models import FormModel
from red.forms import FormForm
from red import views

# Create your views here.
def Index(request):
    form = FormForm()
    
    if request.method == 'POST':
        form = FormForm(request.POST)
        
        if form.is_valid():
            s = form.save()  
            print("Form is saved.....")
            return redirect('/')
        else:
            print("Error.....", form.errors)
    
    context = {'form':form}
    return render (request, 'redcar/index.html', context)