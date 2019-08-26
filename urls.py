from django.conf.urls import url
from . import views

#Add " url(r'^login/', inlcude('apps.login_registration_app')), " to the urlpatterns list in your PROJECTS urls.py file 
urlpatterns = [
    #Access these by putting "/login" in front of them
    url(r'^$', views.log_reg),
    url(r'^success$', views.success),
    url(r'^process_reg$', views.register),
    url(r'^process_log$', views.login),
    url(r'^destroy$', views.logout),
]