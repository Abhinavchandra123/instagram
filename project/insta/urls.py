from re import I
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
# from .views import *
urlpatterns = [
    path('',adminlogin,name='adminlogin'),
    path('home/',home,name='hm'),
    path('viewfetch/',view_fetch,name='fetch'),
    path('viewlist/<pk>',viewlist,name='list')
    # path('')
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)