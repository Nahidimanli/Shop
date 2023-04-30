from django.urls import path
# from core import views
from .views import contact,login,jewellery,index,electronic,fashion
# from django.contrib.auth.views import LoginView

urlpatterns = [
    path('contact/',contact, name='contact'),
    path('login/', login, name='login'),
    path('jewellery/', jewellery, name='jewellery'),
    path('index/',index, name='index'),
    path('electronic/',electronic, name='electronic'),
    path('fashion/', fashion, name='fashion'),



    # path ('blogs', views.blogs, name= 'blogs'),
]

