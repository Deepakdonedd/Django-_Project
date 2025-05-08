from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^userprofile/', views.user, name='userprofile'),
	url(r'^java/', views.javaform, name='javaform'),
    url(r'^drupal/', views.drupalform, name='drupalform'),
    url(r'^node/', views.nodeform, name='nodeform'),
    url(r'^test/', views.userdata, name='userdata'),
    url(r'^cprovider/', views.cloudprovider, name='cprovider'),
    url(r'^thanks/', views.thanks, name='thanks'),
    url(r'^raise_ticket/', views.raise_ticket, name='raise_ticket'),
    url(r'^university-request/$', views.university_request, name='university_request'),
    url(r'^raised-requests/', views.raised_requests, name='raised_requests'),
    url(r'^update-ticket-status/(?P<ticket_id>\d+)/$', views.update_ticket_status, name='update_ticket_status'),
    url(r'^update-request-status/(?P<request_id>\d+)/$', views.update_request_status, name='update_request_status'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
