

from django.urls import path,include
from .import views

urlpatterns = [

    path('',views.homeView,name="home_link"),
    path('gallery/',views.auctiongalleryView,name='auction_gallery_link'),
    path('mydashboard/',views.myDashboardView,name='my_dashboard_link')

]
