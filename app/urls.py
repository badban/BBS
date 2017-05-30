from django.conf.urls import include, url
from app import views

urlpatterns = [

    #url(r'^$', 'app.views.index'),
    #url(r'^index/$', 'app.views.index'),
    #url(r'^detail/(\d+)/$', 'app.views.detail'),
    #url(r'^reg/$', 'app.views.reg'),
    #url(r'^login/$', 'app.views.login'),
    #url(r'logout/$', 'app.views.logout'),
    #url(r'^reply/(\d+)$', 'app.views.reply'),
    #url(r'^user/$', 'app.views.user'),
    #url(r'^post/$', 'app.views.post'),
    #url(r'^category/$', 'app.views.category'),
    #url(r'^category/(\d+)$', 'app.views.node'),
    #url(r'^search/(?P<keyword>.*)/$', 'app.views.search'),
    #url(r'^notifications/$', 'app.views.notifications'),
    


    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^detail/(\d+)/$', views.detail),
    url(r'^reg/$', views.reg),
    url(r'^login/$', views.login),
    url(r'logout/$', views.logout),
    url(r'^reply/(\d+)$', views.reply),
    url(r'^user/$', views.user),
    url(r'^post/$', views.post),
    url(r'^category/$', views.category),
    url(r'^category/(\d+)$', views.node),
    url(r'^search/(?P<keyword>.*)/$', views.search),
    url(r'^notifications/$', views.notifications),
]