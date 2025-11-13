from django.shortcuts import render
from django.views import View
from shop.models import Product
from django.db.models import Q
# Create your views here.
class Search(View):
  def get(self,request):
    query = request.GET['q']
    #print(query)
    if query:
        p = Product.objects.filter(Q(name__icontains=query) | Q(price__icontains=query))
        context = {'items': p}
    return render(request, 'search.html', context)
