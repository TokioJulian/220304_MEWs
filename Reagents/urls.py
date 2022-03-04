from django.urls import path, include
from . import views
from django.contrib import admin

app_name = 'ReagentMaster'

urlpatterns = [
   path('admin/', admin.site.urls),
   path('',  views.Test1.as_view(), name='test1')
]