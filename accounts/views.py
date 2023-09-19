from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['user_name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                # print('username already taken')
                messages.info(request,'Username Already Taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("user created")
                
        else:
            messages.info(request,"Password doesn't match")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
