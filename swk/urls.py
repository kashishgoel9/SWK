from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.HomePage, name = 'homepage'),
    path('aboutus/', views.AboutUs, name = 'aboutus'),
    path('formlayout/',views.formLayout,name='formlayout'),
    path('trackform/', views.TracksheetPage, name = "trackform"),
    path('trackform_det/',views.TrackformPageDetail, name ="trackform_det"),
    path('dutyentryform/', views.DutyEntryPage, name = "dutyentryform"),
    path('login/', views.user_login, name='login'),
    path("logout", views.logout_request, name="logout"),
    path('show/',views.show, name='show'),  
   
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
    # url(r'^download_data/(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})/$', views.download),
    # url(r'^download_data_zone/(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})&(?P<lane_name>\D+)/$', views.downloadzone),
    url(r'^download_data_zone/(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})to(?P<year1>\d{4})-(?P<month1>\d{2})-(?P<day1>\d{2})&(?P<zone_name>\D+)/$', views.downloadzone),
    path('report/',views.report,name='report'),
    path('faq/',views.FAQ, name = 'faq'),
    path('feedback/',views.Feedback, name = 'feedback'),
    path('rating/',views.Rating, name = 'rating'),
    path('contact/',views.Contact, name = 'contact'),
    path('uploadimage/',views.UploadImage, name = 'uploadimage'),
]

