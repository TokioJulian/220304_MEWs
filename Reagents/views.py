from re import template
from django.shortcuts import render
from django.views.generic import (TemplateView,)

# Create your views here.
class Test1(TemplateView):
    template_name = 'reagent_list.html'