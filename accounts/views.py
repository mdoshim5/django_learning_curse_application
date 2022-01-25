from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if (password1 == password2) and len(password1)>3 :
            user = authenticate(request, username=username, password=password1)
            if user is None:
                newuser = User.objects.create_user(username,"", password1)
                newuser.save()
                login(request, newuser)
                return redirect('home')
            else:
                return render(request, 'accounts/signup.html', {'error': "user already exists"})
        else:
            return render(request, 'accounts/signup.html', {'error': "password didn't match"})
    else:
        return render(request, 'accounts/signup.html')


def signin(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', 'home'))
        else:
            return render(request, 'accounts/login.html', {'error': "credetial didn't matched"})
    else:
        return render(request, 'accounts/login.html')


def signout(request):
    logout(request)
    return redirect('home')


def profile(request):
    return render(request, 'accounts/profile.html')


def editprofile(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        print(firstname, lastname)
        user = get_object_or_404(User, pk=request.user.id)
        user.first_name = firstname
        user.last_name = lastname
        user.email = email
        user.save()        
        return redirect('profile')
    else:
        return render(request, 'accounts/editprofile.html')