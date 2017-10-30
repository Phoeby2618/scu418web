from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^scuInfo/',views.scuInforPage,name='testInfor'),
    url(r'^labInfo/',views.labInforPage,name='labInfor'),
    url(r'^information/(?P<infor_id>[0-9]+)$',views.infor,name='infor'),
    url(r'^lifeDay/',views.lifeDayPage,name='lifeOday'),
    url(r'^lifeStudy/',views.lifeStudyPage,name='lifeOstudy'),
    url(r'^resources/',views.resourcesPage,name='resources'),
    url(r'^link/', views.linkPage, name='link'),
    url(r'^schoolstudent/$', views.s_student, name='s_student'),
    url(r'^graduatestudent/$', views.g_student, name='g_student'),
    url(r'^teacher/$', views.getTeacher, name='teacher'),
    url(r'^tprojectlist/$', views.t_project, name='tprojectlist'),
    url(r'^fprojectlist/$', views.f_project, name='fprojectlist'),
    url(r'^tprojectpage/(?P<project_id>[0-99]+)$', views.t_project_page, name='tprojectpage'),
    url(r'^fprojectpage/(?P<project_id>[0-99]+)$', views.f_project_page, name='fprojectpage'),
    url(r'^paperlist/$', views.paperlist, name='paperlist'),
    url(r'^paperpage/(?P<paper_id>[0-99]+)$', views.paperpage, name='paperpage'),
    url(r'^monographlist/$', views.monographlist, name='monographlist'),
    url(r'^monographtpage/(?P<monograph_id>[0-99]+)$', views.monographpage, name='monographpage'),
    url(r'^prizelist/$', views.prizelist, name='prizelist'),
    url(r'^prizepage/(?P<prize_id>[0-99]+)$', views.prizepage, name='prizepage'),
    url(r'^download/(?P<project_id>[0-99]+)$', views.big_file_download, name='download'),
    url(r'^aboutUS/$', views.aboutUs, name='about_us'),
]