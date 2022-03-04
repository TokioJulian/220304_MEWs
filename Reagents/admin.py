from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ( Reagent,)
my_models = ( Reagent, )

# Register your models here.
admin.site.register( my_models )