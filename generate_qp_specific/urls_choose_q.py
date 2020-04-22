from django.conf.urls import url
from .views import choose_question

urlpatterns = [

		url(r'^$',choose_question.as_view(),name = 'choose_question'),

]