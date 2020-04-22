from django.conf.urls import url
from . views import signup

urlpatterns = [

	url(r'^$',signup.as_view(template_name='signup/index.html')),

]