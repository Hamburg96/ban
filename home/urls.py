
from django.conf.urls import url
from home import views


urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^home.html$', views.home, name='home'),
    url(r'^login.html$', views.home, name='login'),
    url(r'^ContactUs$', views.home, name='ContactUs'),
    # url(r'^login$', views.login_view, name='login'),
    # url(r'^logout$', views.logout_view, name='logout'),

]
