from django.conf.urls import url

from logger import views

urlpatterns = [
    url(r'^$', views.InvestigationList.as_view(), name='index'),
    url(r'investigation/add/$', views.InvestigationCreate.as_view(),
        name='investigation-add'),
    url(r'investigation/(?P<pk>[0-9]+)/$', views.InvestigationDetail.as_view(),
        name='investigation-detail')

]
