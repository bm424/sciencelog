from django.conf.urls import url

from logger import views

urlpatterns = [
    url(r'^$', views.InvestigationList.as_view(), name='index'),
    url(r'^investigations/$', views.InvestigationList.as_view(),
        name='investigation-list'),
    url(r'investigations/add/$', views.InvestigationCreate.as_view(),
        name='investigation-add'),
    url(r'investigations/(?P<slug>[-\w]+)/$', views.InvestigationDetail.as_view(),
        name='investigation-detail'),
    url(r'investigations/(?P<slug>[-\w]+)/logs/$', views.LogList.as_view(),
        name='investigation-logs'),
    url(r'investigations/(?P<slug>[-\w]+)/logs/add/$', views.LogCreate.as_view(),
        name='investigation-logs-add'),
    url(r'investigations/(?P<slug>[-\w]+)/logs/(?P<pk>[0-9]+)/',
        views.LogDetail.as_view(),
        name='investigation-logs-detail'),
    url(r'logs/(?P<pk>[0-9]+)/update/',
        views.LogUpdate.as_view(),
        name='investigation-logs-update'),
    url(r'logs/$', views.LogList.as_view(), name='logs'),
    url(r'logs/add/$', views.LogCreate.as_view(), name='logs-add'),
    url(r'images/$', views.ImageList.as_view(), name='images'),
    url(r'images/add/', views.ImageCreate.as_view(), name='images-add'),
    url(r'images/(?P<slug>[-\w]+)/', views.ImageDetail.as_view(),
        name='images-detail'),

]
