from django.conf.urls import include, url
from django.contrib import admin
from jsPartner.users import views

urlpatterns = [
    # Examples:
    url(r'^$', 'views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/signup/$', 'jsPartner.users.views.signup', name="signup"),
    url(r'^user/user_signup/$', 'jsPartner.users.views.user_signup', name="user_signup"),
]
