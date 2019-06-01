
from django.conf.urls import url

from . views import EmailVerifyRecodeView,Loginview,RegisterView,Userlistview,UserPut,Resetview



urlpatterns = [
    url(r'^DoLogin/', Loginview.as_view(),name='DoLogin'),
    url(r'^EmailVerifyRecode/',EmailVerifyRecodeView.as_view(),name='EmailVerifyRecode'),
    url(r'^Register/', RegisterView.as_view(),name='Register'),
    url(r'^Userlist/', Userlistview.as_view(),name='Userlist'),
    url(r'^UserPut/', UserPut.as_view(),name='UserPut'),
    url(r'^Resetview/',Resetview.as_view(),name = 'Resetview'),

]