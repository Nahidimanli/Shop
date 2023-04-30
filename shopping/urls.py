"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from core.views import fashion, index, jewellery, login, electronic
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static
from core.urls import urlpatterns as core_urls
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name= 'index'),
    path('fashion/',fashion, name = 'fashion'),
    path('contact/', views.contact, name='contact'),
    path('jewellery/',jewellery, name = 'jewellery'),
    path('electronic/',electronic, name = 'electronic'),

    path('login',login, name = 'login'),
    path('index',index, name = 'index'),
    path('', include('social_django.urls', namespace='social')),
    path('', include(core_urls)),
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 






