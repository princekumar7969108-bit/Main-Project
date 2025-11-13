from django.shortcuts import render,redirect
from django.views import View
from . models import Category_items,Product
from .forms import SignupForm,LoginForm,CategoryForm,ProductForm,StockForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
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




class ProductDetail(View):
    def get(self,request,i):
        a=Product.objects.get(id=i)
        context={'product':a}
        return render(request,'productdetail.html',context)


class Register(View):
    def get(self,request):
         form_instance=SignupForm()
         context= {'form':form_instance}
         return render(request,'register.html',context)

    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:login')


class Login(View):
    def get(self, request):
        form_instance = LoginForm()
        context={'form':form_instance}
        return render(request, 'login.html',context)

    def post(self,request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.cleaned_data['username']
            p=form_instance.cleaned_data['password']
            user=authenticate(username=u,password=p)

            if user and user.is_superuser==True:
                login(request,user)
                return redirect('shop:adminpage')
            elif user:
                login(request,user)
                return redirect('shop:categories')
            else:
                messages.error(request, 'invalid user credentials')
                return render(request, 'login.html', {'form': form_instance})


class Logout(View):
  def get(self,request):
      logout(request)
      return redirect('shop:login')

class Admin(View):
   def get(self, request):
      return render(request,'adminpage.html')

class AddCategory(View):
    def get(self,request):
     form_instance=CategoryForm()
     context={'form':form_instance}
     return render(request,'addcategory.html',context)

    def post(self,request):
        form_instance=CategoryForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:categories')
        else:
            print('error')
            return render(request, 'addcategory.html', {'form': form_instance})


class AddProducts(View):
    def get(self,request):
     form_instance=ProductForm()
     context={'form':form_instance}
     return render(request,'addproduct.html',context)

    def post(self,request):
        form_instance=ProductForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:categories')
        else:
            print('error')
            return render(request, 'addproduct.html', {'form': form_instance})
class Stock(View):
    def get(self,request,i):
        s=Product.objects.get(id=i)
        form_instance=StockForm(instance=s)
        context={'stock':form_instance}
        return render(request,'addstock.html',context)

    def post(self, request, i):
        s = Product.objects.get(id=i)
        form_instance = StockForm(request.POST, instance=s)
        if (form_instance.is_valid()):
            form_instance.save()
            return redirect('shop:categories')
