from django.shortcuts import render, redirect
from django.contrib.auth.admin import UserCreationForm
from django.contrib import messages
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def userRegister(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'user {username} registered succesfully')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    #    ndersa ne rastin e post kerkeses me ane te request.POST marrim te dhenat e reja qe vendos useri
    # ndersa instancat i lejme ne menyre qe te dim se cilin perdorues duhet te updetojme
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # request.FILES meqenese do uploadim file image
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        username = request.user.username
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'user {username} updated succesfully')
            return redirect('user-profile')
    else:
        # instance user dhe profile ne menyre qe te na shfaqen te dhenat e userit aktual dhe te dhenat qe dum te ndryshojm
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'users/profile.html', context)
