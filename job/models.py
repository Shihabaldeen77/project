from distutils import extension
from distutils.command import upload
from unicodedata import category
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

JOP_TYPE=(
    ('FULL TIME','FULL TIME'),
    ('PART TIME','PART TIME'),

)

def uploadiam(instance,filename):
    imagename ,extension =filename.split(".")
    return "job/%s/%s.%s"%(instance.id,instance.id,instance)



class Job(models.Model):
    owner=models.ForeignKey(User,related_name="jop_owner",on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    jop_type=models.CharField(max_length=20,choices=JOP_TYPE)
    puplishat=models.DateTimeField(auto_now=True)
    salary=models.IntegerField(default=1)
    experiance=models.IntegerField(default=5)
    vecancy=models.IntegerField(default=1)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to=uploadiam)
    slug=models.SlugField(blank=True,null=True)

    categori=models.ForeignKey('Categoryies',on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Categoryies(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Apply(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    vewsite=models.URLField()
    cv=models.FileField(upload_to="Apply/")
    couver_letter=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now=True)
    jop=models.ForeignKey(Job,on_delete=models.CASCADE,related_name="applay_job")
    def __str__(self):
       return self.name