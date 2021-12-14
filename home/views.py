from django.shortcuts import render
from .models import *
from django.views.generic import View

class BaseView(View):
    views = {}





class Homeview(BaseView):
    def get(self,request):




        return render(request,'index.html',self.views)
