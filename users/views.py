from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ProfileUpdateForm, UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Created for {username}')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request , 'users/register.html' , {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_from = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_from.is_valid() and p_form.is_valid():
            u_from.save()
            p_form.save()
            username = u_from.cleaned_data.get('username')
            messages.success(request,f"{username}'s account has been updated")
            return redirect('profile')
    else:
        u_from = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()
    context = {
        'u_form' : u_from,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html',context)