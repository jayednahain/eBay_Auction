
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop_app.urls')),
    path('members/',include('members.urls')),
    path('authentication/',include('authentication_system.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
