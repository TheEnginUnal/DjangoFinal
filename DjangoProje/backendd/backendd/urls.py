
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from Article import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='home'),
    path('shopcart/',views.shopcart),
    path('user/',include('user.urls', namespace='user')),
    path('product/',include('product.urls', namespace='product')),
    path('search/',include('Article.urls', namespace='article')),
    path('store/',include('store.urls', namespace='store')),
    path('payment/',include('payment.urls', namespace='payment')),

   
   
    


    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)