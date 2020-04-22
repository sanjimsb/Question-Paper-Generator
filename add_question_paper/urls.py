from django.conf.urls import url
from add_question_paper.views import add_question_main
# from .  import views


urlpatterns = [

	url(r'^$',add_question_main.as_view(),name ='add_question_main'),
	# url(r'^$',views.start,name ='add_question_main'),

]