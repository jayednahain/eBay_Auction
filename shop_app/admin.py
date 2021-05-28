from django.contrib import admin
from .models import AuctionItem,Category

# Register your models here.


admin.site.register(AuctionItem)
admin.site.register(Category)

