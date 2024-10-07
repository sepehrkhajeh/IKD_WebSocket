from django.shortcuts import render,HttpResponse
from django.views.generic import View
# Create your views here.
class WS_View(View):
    
    def get(self,request,code):
        print(code)
        return HttpResponse(
            f'you are {code}'
        )