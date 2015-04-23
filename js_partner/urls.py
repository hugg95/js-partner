from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'js_partner.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/signup/$', 'js_user.views.signup', name='signup'),
    url(r'^user/login/$', 'js_user.views.login', name='login'),
    url(r'^user/change_password/$', 'js_user.views.change_password', name='change_password'),
]
