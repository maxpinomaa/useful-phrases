from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/reverse/$', views.reverse_list, name='reverse_list'),
    url(r'^fincc1/$', views.post_list1, name='post_list1'),
    url(r'^fincc2/$', views.post_list2, name='post_list2'),
    url(r'^finruscc1/$', views.post_list3, name='post_list3'),
    url(r'^engitacc1/$', views.post_list4, name='post_list4'),
    url(r'^engitacc2/$', views.post_list5, name='post_list5'),
    url(r'^fincomics/$', views.post_list6, name='post_list6'),
    url(r'^finfunint/$', views.post_list7, name='post_list7'),
]