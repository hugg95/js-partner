from django.conf.urls import include, url
from django.contrib import admin
import demo

urlpatterns = [
    # Examples:
    url(r'^$', 'views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^hello/$', include(views.hello)),
    url(r'^hello/', 'demo.views.hello', name="hello"),
    url(r'^demo/', 'demo.views.demo', name="demo"),
]
