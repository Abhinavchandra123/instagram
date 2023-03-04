from django.contrib import admin

# Register your models here.
from .models import insta,Category,Searchid

admin.site.register(insta)
admin.site.register(Category)
admin.site.register(Searchid)