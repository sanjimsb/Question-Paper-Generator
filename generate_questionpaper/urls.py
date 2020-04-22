from django.conf.urls import url, include
from . views import generate_question_paper

urlpatterns = [
	
	url(r'^$',generate_question_paper.as_view(),name = 'generate_question_paper'),

]