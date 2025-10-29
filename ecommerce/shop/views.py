from django.shortcuts import render
from django.views import View
from . models import Category_items,Product
# Create your views here.

class Categories(View):
    def get(self,request):
        a=Category_items.objects.all()
        context={'category':a}
        return render(request,'categories.html',context)


class Products(View):
    def get(self, request,i):
        c=Category_items.objects.get(id=i)
        context={'category':c}

        return render(request, 'product.html',context)