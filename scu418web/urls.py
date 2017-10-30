"""scu418web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from lab.views import homepage,brief_introduction_of_laboratory,test
from forum.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetPwdView, ModifyView, ForumView

urlpatterns = [
    url(r'^$', homepage),
    url(r'test/$', test),
    url(r'^brief_introduction_of_laboratory/$', brief_introduction_of_laboratory),
    url(r'^admin/', admin.site.urls),

    url(r'^captcha/', include('captcha.urls')),
    url(r'^forum/$', ForumView.as_view(),name='forumIndex'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='active'),
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget'),
    url(r'^reset/(?P<reset_code>.*)/$', ResetPwdView.as_view(), name='reset'),
    url(r'^modify/$', ModifyView.as_view(), name='modify'),

    url(r'^lab/', include('lab.urls', namespace='lab'))
]
