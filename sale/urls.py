from django.conf.urls import url
from django.urls import path,re_path
from .views import *

app_name = 'sale'

urlpatterns = [
    path('plus-sale',plus_view,name='plus'),
    # path('plus-detail<int:id/>', detail_view,name='detail'),
    path('rent', rent_view,name='rent'),
    path('game', game_view,name='game'),
    path('psn-sale', psn_view,name='psn'),
    url(r'^(?P<id>[\w-]+)/plus-detail/$', detail_view, name="detail"),
    url(r'^(?P<id>[\w-]+)/game-detail/$', game_detail, name="gamedetail"),
    url(r'^(?P<id>[\w-]+)/psn-detail/$', psn_detail_view, name="psn-detail"),

]
