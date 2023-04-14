from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from main.models import FavoriteList
from users.forms import CustomUserCreationForm, UserEdit

# Create your views here.
def registration(request):
    context = {}
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=email, password=raw_password)
            FavoriteList.objects.create(user=account)
            login(request, account)
            return redirect("users:profile_edit")
        else:
            context['registration_form'] = form
    else:
        form = CustomUserCreationForm()
    return render(request=request, template_name="users/registration.html", context={"register_form": form})


def login_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("users:profile")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="users/login.html", context={"login_form": form})


@login_required
def profile(request):
    favorite_list = FavoriteList.objects.get(user=request.user).products.all()
    context = {
        'favorite_list': favorite_list
    }
    return render(request, 'users/profile.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login_in')


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserEdit(request.POST, instance=request.user)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('users:profile')
    else:
        form = UserEdit(instance=request.user)
    return render(request, 'users/changePersonInformation.html', {'form': form})

