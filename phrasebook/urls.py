from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^finnish/common_questions$', views.reverse_list, name='reverse_list'),
    url(r'^finnish/conversational/$', views.post_list1, name='post_list1'),
    url(r'^finnish/conversational2/$', views.post_list2, name='post_list2'),
    url(r'^finskiy/finruscc1/$', views.post_list3, name='post_list3'),
    url(r'^italian/conversational/$', views.post_list4, name='post_list4'),
    url(r'^italian/conversational2/$', views.post_list5, name='post_list5'),
    url(r'^fincomics/$', views.post_list6, name='post_list6'),
    url(r'^finnish/fun_interesting/$', views.post_list7, name='post_list7'),
    url(r'^finskiy/$', views.post_list8, name='post_list8'),
    url(r'^finskiy/rusfinfun/$', views.post_list9, name='post_list9'),
    url(r'^italian/$', views.post_list10, name='post_list10'),
    url(r'^spanish/$', views.post_list11, name='post_list11'),
    url(r'^spanish/funint$', views.post_list12, name='post_list12'),
    url(r'^finskiy/common_questions$', views.post_list13, name='post_list13'),
    url(r'^finskiy/finruscc2/$', views.post_list14, name='post_list14'),
    url(r'^spanish/conversational/$', views.post_list15, name='post_list15'),
    url(r'^italian/common_questions/$', views.post_list16, name='post_list16'),
    url(r'^italian/fun_interesting/$', views.post_list17, name='post_list17'),
]