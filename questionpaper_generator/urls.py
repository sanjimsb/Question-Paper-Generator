"""questionpaper_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from signup.views import signup
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^add_question_paper/',include('add_question_paper.urls')),
    url(r'^signup/',signup.as_view(template_name = 'signup/index.html')),
    # url(r'^',include('login.urls')),
    url(r'^$',auth_views.LoginView.as_view(template_name='login/index.html'),name='login'),
    url(r'^logout/',auth_views.LogoutView.as_view(template_name='logout/index.html'),name='logout'),
    url(r'^generate_qp/',include('generate_questionpaper.urls')),
    url(r'^generate_qp_specific/',include('generate_qp_specific.urls')),
    url(r'^choose_question/',include('generate_qp_specific.urls_choose_q'))

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)