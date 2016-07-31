from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_post/(?P<thread_id>[0-9]+)/$', views.create_post, name='create_post'),
    url(r'^create_thread/$', views.create_thread, name='create_thread'),
]
