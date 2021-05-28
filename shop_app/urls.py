

from django.urls import path,include
from .import views
from shop_app.class_based_views import createPorductView,editProductView,singleProductView,deleteProductView


urlpatterns = [

    path('',views.homeView,name="home_link"),
    path('gallery/',views.auctiongalleryView,name='auction_gallery_link'),
    path('mydashboard/',views.myDashboardView,name='my_dashboard_link'),

    #product CRUR operation
    path('createproduct/',createPorductView.as_view(),name="create_product_link"),
    path('view_product/<int:pk>',singleProductView.as_view(),name='singe_product_view_link'),
    path('editproduct/<int:pk>',editProductView.as_view(),name='edit_product_link'),
    path('deleteproduct/<int:pk>',deleteProductView.as_view(),name='delete_product_link'),
    path('categoryview/<str:cats_name>',views.cateogryView,name='category_view_link'),
    path('test/',views.test_theme,name='test_link')


]
