from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from login import views

urlpatterns = [
    url(r'^login/$', views.registereduser,name='registereduser'),
    url(r'^register/$', views.registration,name='registration'),
    url(r'^login/userdetails/(?P<pk>[0-9]+)$', views.user_details),
    url(r'^login/signup/$',views.signupPage),
   # url(r'^login/(?P<phonenumber>(\d+))$', views.onlogin),
    url(r'^login/userlogin/$',views.loginpage),
    url(r'^loginuser/$',views.user_login,name='user_login'),
    url(r'^login/check/$',views.logincheck),
    url(r'^loginuser/cheking/$',views.checkfor_loggedinuser,name='checkfor_loggedinuser'),
    url(r'^login/logout/$',views.logout_user),
    url(r'^loginuser/log/$',views.user_logout,name='user_logout'),
    url(r'^login/sms/$',views.sms),
    url(r'^login/sms3/$',views.sms3),
    url(r'^login/vendors/$',views.vendor_list,name='vendor_list'),
    url(r'^login/visitor/$',views.visitor,name='visitor'),
    url(r'^login/addvisitor/$',views.addnewvisitor,name='addnewvisitor'),
    url(r'^login/send_pin/$',views.send_pin),
]

urlpatterns = format_suffix_patterns(urlpatterns)
