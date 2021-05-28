
from django.views.generic import DeleteView,ListView,DetailView,CreateView,UpdateView
from .models import AuctionItem
from .forms import ProductCreateFrom,ProductUpdateForm
from django.urls import reverse_lazy


class createPorductView(CreateView):
   model = AuctionItem
   template_name = "create_Auction_item.html"
   #fields = '__all__' #use for select all the field
   #fields = ('title','body') #selected field
   form_class = ProductCreateFrom


class editProductView(UpdateView):
   model = AuctionItem
   template_name = 'update_auction_item.html'
   form_class = ProductUpdateForm

class singleProductView(DetailView):
   model = AuctionItem
   template_name = 'product_profile.html'



class deleteProductView(DeleteView):
   model = AuctionItem
   template_name = 'delete_product.html'
   success_url = reverse_lazy('auction_gallery_link')

