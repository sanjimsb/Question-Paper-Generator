from django.conf.urls import include, url
from login.views import login
from add_question_paper.urls import question_main
from django.contrib.auth import views as auth_views
from signup.urls import signup

urlpatterns = [
		url(r'^$',auth_views.LoginView.as_view(template_name = 'login/index.html')),
		url(r'^add_question_paper/',question_main.as_view()),
		url(r'^signup/',signup.as_view(template_name='signup/index.html')),

]