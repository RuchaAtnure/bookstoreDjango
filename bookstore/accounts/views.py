from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'Invalid credentials')
            return redirect(login)
    else:
        return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['PASS1']
        password2 = request.POST['PASS2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,
                                                password = password1 , email=email)
                user.save();
                print('user created')
                return redirect('login')
        else:
             messages.info(request, 'Password not matching')
             return redirect('signup')
        return redirect('/')
    else:
        return render(request , 'signup.html')

def logout(request):
    auth.logout(request);
    return redirect('/')