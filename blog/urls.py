from django.conf.urls import url
import views

urlpatterns = [
    url(r'^blog/$', views.post_list, name='blog_post'),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
]
