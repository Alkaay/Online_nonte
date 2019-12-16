"""Определяет схемы URL для learning_logs."""
from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'

urlpatterns = [
	# Страница входа
	# url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
	path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
	url(r'^logout/$', views.logout_view, name='logout'),
	# Страница регистрации
	url(r'^register/$', views.register, name='register'),
]
