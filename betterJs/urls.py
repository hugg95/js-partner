from django.conf.urls import include, url
from django.contrib import admin
from user import views

urlpatterns = [
    # Examples:
    url(r'^$', 'views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/signup/$', 'user.views.signup', name="signup"),
    url(r'^user/user_signup/$', 'user.views.user_signup', name="user_signup"),
]
