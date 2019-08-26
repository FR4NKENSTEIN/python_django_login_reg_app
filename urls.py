from django.conf.urls import url
from . import views

#Add " url(r'^', inlcude('apps.login_registration_app')), " to the urlpatterns list in your PROJECTS urls.py file 
urlpatterns = [
    url(r'^$', views.log_reg),
    url(r'^success$', views.success),
    url(r'^process_reg$', views.register),
    url(r'^process_log$', views.login),
    url(r'^destroy$', views.logout),
]