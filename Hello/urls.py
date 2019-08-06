from django.conf.urls import url

from .views import Controller

urlpatterns = [
    url(r'^$', Controller.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', Controller.room, name='room'),
]