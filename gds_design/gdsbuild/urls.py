from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='gdsbuild_home'),
	path('base', views.base, name='gdsbuild_base'),
	# path('signup_test', views.signup_test, name='signup_test'),
	path('signup', views.signup, name='signup'),
	path('form_tester', views.form_tester, name='form_tester'),
	path('home', views.home, name='home'),
	path('split', views.split, name='split'),
	path('login', views.login, name='login'),
	path('help', views.help, name='help'),

	path('simple_signup', views.simple_signup, name='simple_signup'),
	path('logout', views.logout, name='logout'),

# Split style using includes
	path('split_home', views.split_home, name='split_home'),

]