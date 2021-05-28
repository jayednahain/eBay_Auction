from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from .models import AuctionItem
from .forms import ProductCreateFrom

# Create your views here.
def homeView(request):
   return render(request,'shop.html')

def auctiongalleryView(request):
   data = AuctionItem.objects.all()

   return render(request,'action_glellary.html',{"data":data})


def myDashboardView(request):
   return render(request,'my_Dashboard.html')


def cateogryView(request,cats_name):
   return render(request,'product_category_view.html',{"category":cats_name})



def test_theme(request):
   return render(request,'test_theme.html',{})




