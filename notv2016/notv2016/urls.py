"""notv2016 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

from django.contrib.auth.views import login, logout, password_reset, password_reset_done, \
    password_reset_confirm, password_reset_complete
from users.views import register_user, account, index, password_change, NOTVUserUpdate


urlpatterns = patterns(
    '',
    url(r'^notv/', include(patterns(
        '',

        url(r'^login/$', login, {"template_name": "login.html"}),
        url(r'^logout/$', logout, {"next_page": "/notv/account"}),
        url(r'^register/$', register_user),
        url(r'^events/$', index),
        url(r'^account/$', account),
        url(r'^account/update/$', NOTVUserUpdate.as_view(template_name='notvuser_form.html', success_url="/account/")),
        url(r'^password/change/$', password_change,
            {"post_change_redirect": "notv/user/password/done"}),
        url(r'^user/password/reset/$', password_reset,
            {'post_reset_redirect': '/notv/user/password/reset/done/',
                'email_template_name': 'password_reset_email.html',
                "template_name": "password_reset_form.html"}, name="password_reset"),
        url(r'^user/password/reset/done/$', password_reset_done,
            {"template_name": "password_reset_done.html",
                "post_change_redirect": "notv/user/password/done"},
            ),
        url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'password_change_form.html',  'post_reset_redirect': '/notv/logout/'}),
        url(r'^user/password/done/$', password_reset_complete,
            {"template_name": "password_reset_complete.html"}),
        url(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}
            ),
    ),
    )))

urlpatterns += patterns(
    '',
    url(r'^notv/admin/', admin.site.urls),
    )
