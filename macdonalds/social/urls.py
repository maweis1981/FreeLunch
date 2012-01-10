from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'social.views.index', name='index'),
    url(r'^weibo', 'social.views.weiboValidate', name='weibo'),    
    url(r'^token', 'social.views.weiboAccessToken', name='token'),    
    url(r'^callback', 'social.views.callback', name='callback'),        
    url(r'^update', 'social.views.updateUserInfo', name='updateUserInfo'),  
    url(r'^friends', 'social.views.loadFriendsFromWeibo', name='loadFriendsFromWeibo'),      
              
)
