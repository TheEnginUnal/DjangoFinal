
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from Article import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='home'),
    path('shopcart/',views.shopcart),
    path('user/',include('user.urls')),
    path('product/',include('product.urls')),
    path('search/',include('Article.urls'))
   
    


    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)