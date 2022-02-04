from functools import wraps
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.



def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,username=username,password = password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return render(request,"account/login.html",{
                "error" :"Kullanıcı adı veya parola hatalı"
            })

    elif request.method == "GET":
        return render(request,"account/login.html")
    else:
        return render(request,"account/login.html",{
            "error" : "Bu method izin verilmez ! "
        })

    



def register_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        checkUserForRegistration(request,username,password,repassword,email)
        createUserandReturnToLogin(username,email,firstname,lastname,password)

    return render(request,"account/register.html",{
        "info" : "Hesabınız başarıyla oluşturulmuştur"
    })



def checkUserForRegistration(request,username,password,repassword,email):

    if password != repassword:
        return render(request,"account/register.html",{
            "error" :"Parola bölümleri eşleşmiyor ! "
        })

    if User.objects.filter(username = username).exists():
        return render(request,"account/register.html",{
            "error" : "Bu kullanıcı adına ait başka bir kullanıcı kaydı bulunuyor!"
        })

    if User.objects.filter(email = email).exists():
        return render(request,"account/register.html",{
            "error" : "Bu maile sahip başka bir kullanıcı kaydı bulunuyor!"
        })



def createUserandReturnToLogin(username,email,firstname,lastname,password):
    user = User.objects.create_user(username=username,email = email,first_name = firstname,last_name = lastname,password=password)
    user.save()
    return redirect("login")



@login_required
def logout_request(request):
    logout(request)
    return redirect("login")



