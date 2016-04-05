from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', journalview, name = "journallist"),
	url(r'^create$', createview, name = "create"),
	url(r'^(?P<pk>\d+)$', detailview, name = "detail"),
	url(r'^(?P<pk>\d+)/update', updateview),
	url(r'^(?P<pk>\d+)/delete', deleteview)
	]
