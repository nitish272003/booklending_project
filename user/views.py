from django.shortcuts import render,redirect
from . forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Hi {username}, account creation successful')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request,'signup.html',{
        'form':form,
    })

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')

