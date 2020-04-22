from django.conf.urls import url
from . views import qp_choice_generate

urlpatterns = [
		url(r'^$',qp_choice_generate.as_view(),name = 'qp_choice_generate'),

]