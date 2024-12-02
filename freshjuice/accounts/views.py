from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages
from django.shortcuts import render, redirect


def signup(request):
    template_name = 'accounts/signup.html'
    return render(request, template_name)


def password_reset(request):
    template_name = 'accounts/password_reset.html'
    return render(request, template_name)


@login_required
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('accounts:profile')  # Redirect to home or any other page
        else:
            return redirect('accounts:edit_profile')
    else:
        form = UserProfileForm()

    return render(request, 'accounts/create_profile.html', {'form': form})


def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')  # Redirect to profile page after saving
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})



def accounts(request):
    template_name = 'accounts/accounts.html'
    return render(request, template_name)


@login_required
def profile_view(request):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        # Handle the case where the profile does not exist
        return redirect('accounts:create_profile')  # Redirect to a view where the user can create their profile
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})

@login_required
def profile_edit(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'accounts/profile_edit.html', {'form': form})


def settings(request):
    template_name = 'accounts/settings.html'
    return render(request, template_name)


def activity_log(request):
    template_name = 'accounts/activity_log.html'
    return render(request, template_name)


def logout_view(request):
    logout(request)
    return redirect('home:home')


def register(request):
    template_name = 'dashboard/register.html'
    return render(request, template_name)


def signup_view(request):
    template_name='dashboard/register.html'
    return render(request, template_name)


def login_view(request):
    template_name = 'dashboard/login.html'
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect('dashboard')
        else:
            messages.success(request, 'incorrect username or password')
            return redirect('accounts:login')
    else:
        return render(request, template_name)


def contact_support(request):
    template_name = 'accounts/contact_support.html'
    return render(request, template_name)