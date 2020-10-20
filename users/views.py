from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def RegisterUser(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # data bounded in form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f'{username} your Account has been created! Now you are abble to login')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def profile(request):
    return render(request, 'users/profile.html',)
