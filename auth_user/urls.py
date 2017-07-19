from django.conf.urls import url
from . import views
from auth_user import views
app_name = 'auth_user'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^$', views.logout_user, name='logout_user'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username')]
