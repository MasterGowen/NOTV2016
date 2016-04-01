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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from django.contrib.auth.views import login, logout
from users.views import register_user, account

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns.append(url(r'^rosetta/', include('rosetta.urls')))

# AAA
urlpatterns += (
    url(r'^login/', login, {"template_name": "login.html"}),
    url(r'^logout/', logout, {"next_page": "/"}),
    url(r'^register/', register_user),
    url(r'^$', account),
)

