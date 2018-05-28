from django.conf.urls import url
from . import views

urlpatterns = [
   
    url(r'^$', views.index, name='index'),
	url(r'^second/$', views.second, name='second'),
	url(r'^third/$', views.third, name='third')
    
]
