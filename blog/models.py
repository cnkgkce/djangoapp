from tkinter import CASCADE
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

# images/blogs/1.jpg --> blogs 'upload_to =...' değişkeninden geliyor images'ı ise settings.py dosyasında 
# takma isim olarak belirttik. Yani ana dizinde uploads klasörünü göstermeyeceğim onun yerine images göstericem ikinci kısım ise path'dir bu da upload_to ya denk gelir

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=True,blank=True,unique=True,db_index=True,editable=False)


    def __str__(self) -> str:
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        return super().save(*args,**kwargs)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "blogs")
    description = RichTextField()
    is_active = models.BooleanField()
    is_home = models.BooleanField()
    slug = models.SlugField(null=False,blank=True ,unique=True, db_index=True,editable=False)  #blank=True olayı django admin panelinde bir zorunluluk olmaması açısından kullanılır. Null ise veritabanıyla ilgili bir parametredir 
    #category = models.ForeignKey(Category, default = 1 ,on_delete=models.CASCADE)   --> one to many ilişkisi içindir 
    categories = models.ManyToManyField(Category, blank=True)



    def __str__(self) -> str:
        return f"{self.title}"

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        return super().save(*args,**kwargs)


