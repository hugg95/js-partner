from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'js_partner.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^user/signup/$', 'js_partner.views.signup', name="signup"),
    url(r'^user/signup/$', 'js_user.views.signup', name='signup')
]
