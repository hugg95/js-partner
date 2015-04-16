from django.conf.urls import include, url
from django.contrib import admin
import user

urlpatterns = [
    # Examples:
    url(r'^$', 'views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/signup/', 'user.views.signup', name="signup"),
]
