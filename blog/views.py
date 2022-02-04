from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog,Category
from django.contrib.auth.decorators import login_required

# Create your views here.

#Örnek dinamik bir veri seti oluşturalım diğer aşamada zaten veritabanı ile çalışacağız
# data = {
#     "blogs" :[
#        {
#            "id" : 1,
#            "title" : "Web Geliştirme Kursu",
#            "image" : "1.jpg",
#            "is_active" : False,
#            "is_home" : True,
#            "description" : "güzel bir kurs",

#        },

#              {
#            "id" : 2,
#            "title" : "Mobil Geliştirme Kursu",
#            "image" : "2.jpg",
#            "is_active" : True,
#            "is_home" : False,
#            "description" : "idare eder",

#        },
#              {
#            "id" : 3,
#            "title" : "Siber güvenlik Kursu",
#            "image" : "3.jpg",
#            "is_active" : True,
#            "is_home" : True,
#            "description" : "şahane kurrss yaavvv",

#        } 
#     ]
# }



@login_required(login_url ="account/login") #tüm templatesleri bulur 
def index(request):
    context = {
        "blogs" : Blog.objects.filter(is_home = True, is_active=True),
        "categories" : Category.objects.all(),
    }
    return render(request,"blog/index.html",context)


@login_required(login_url ="account/login")
def blogs(request):
    context = {
        "blogs" : Blog.objects.filter(is_active = True),
        "categories" : Category.objects.all(),
    }
    return render(request,"blog/blogs.html",context)


@login_required(login_url ="account/login")
def blogDetails(request,slug):  #Bu slug bilgisi veya id bilgisi HTML üzerinden geliyor kısaca _blog.html > blog details adındaki URL tetiklenir > ardından bu metod tetiklenir 
 
    blog = Blog.objects.get(slug=slug) # Blog.objects.get() ile Blog.objects.filter() arasındaki fark şudur.filter da bir liste dönerken get metodunda sadece tek bir model dönmektedir
    
    return render(request,"blog/blog-details.html",{"selectedBlog" : blog})



@login_required(login_url ="account/login")
def blogs_by_category(request,slug):
    context = {
        "blogs" : Category.objects.get(slug=slug).blog_set.all(),   #category__slug = slug yapısı aslında blog yapısının category ile relate edilmesi ile ortaya çıkıyor 
        "categories" : Category.objects.all(),
        "selectedSlug" : slug,
    }

    return render(request,"blog/blogs.html",context)

