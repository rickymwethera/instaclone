from django.conf.urls import url, include
from . import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^profile/',views.profile,name = 'profile'),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'post/newimage/',views.create_post,name = 'create'),
    url(r'like/(\d+)',views.like_post,name = 'like'),
    url('follow-unfollow/',views.follow_unfollow,name = 'follow-unfollow-view'),

    
] 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)