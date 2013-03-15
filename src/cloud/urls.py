from django.conf.urls import patterns, include, url

urlpatterns = patterns('cloud.views',
    url(r'^$', 'index'),#main/landing page? login?
    url(r'^status_report/$', 'status_report'),
    #url(r'^/', ),#profile page
    #url(r'^/', ),#app1 view
    #url(r'^/', ),#app2 view
)
