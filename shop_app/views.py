from django.shortcuts import render

# Create your views here.
def homeView(request):
   return render(request,'shop.html')

def auctiongalleryView(request):
   return render(request,'action_glellary.html')


def myDashboardView(request):
   return render(request,'my_Dashboard.html')