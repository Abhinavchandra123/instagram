from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    types=models.CharField(max_length=100,null=False,blank=False)

class Searchid(models.Model):
    class Meta:
        verbose_name = 'Searchid'
        verbose_name_plural = 'searchids'
    userid=models.CharField(max_length=60,null=False,blank=False)

class insta(models.Model):
    class Meta:
        verbose_name = 'insta'
        verbose_name_plural = 'instas'
    accound=models.CharField(max_length=50,null=True,blank=True)
    username=models.CharField(max_length=200,blank=False)
    dp=models.ImageField(blank=False,null=False)
    question=models.CharField(max_length=500,null=True,blank=True)
    answer=models.CharField(max_length=100,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL, null=True,blank=True)
    Search=models.ForeignKey(Searchid,on_delete=models.SET_NULL,null=True,blank=True)
    loguser=models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)

