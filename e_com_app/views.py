from django.shortcuts import render
from django.views.generic import View
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from .models import  Product


# Create your views here.
class HomeView(View):
    def get(self, *args, **kwargs):
        # We have to get the data from the DB, for example: products

        products = Product.objects.all().values()
        context = {
            'products': products
        }


        return render(self.request, "index.html", context)
    
class StoreView(View):
    def get(self,request,*args, **kwargs):
        # We have to get the data from the DB, for example: products
        category =  request.GET.get('category', '')
        if(category==''):
            products = Product.objects.all().values()
        else:
            category=category+"\n"
            products = Product.objects.filter(Productcategorie=category).values()

        context = {
            'products': products
        }

        print(context)
    

        return render(self.request, "store.html", context)
    
class ProductView(View):
    def get(self,request, *args, **kwargs):
        # We have to get the data from the DB, for example: products
        product = Product.objects.get(pk=request.GET.get('id',''))
        

        context = {
            'product': product
        }
    

        return render(self.request, "product.html", context)
      
class BlankView(View):
    def get(self, *args, **kwargs):
        # We have to get the data from the DB, for example: products

        products = Product.objects.all().values()

        context = {
            'products': products
        }
    

        return render(self.request, "blank.html", context)

class FindView(View):
    def get(self,request):
        query = request.GET.get('q', '')
        vector = SearchVector('label', config='english')
        search_query = SearchQuery(query, config='english')
        products = Product.objects.annotate(rank=SearchRank(vector, search_query)).filter(rank__gte=0.00000000000000000000001).order_by('-rank')
        print(products)
        context = {
            'products': products
        }   

        
        return render(request, 'store.html', context)
