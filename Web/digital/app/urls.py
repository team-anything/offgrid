from django.conf.urls import url
from app import views

# SET THE NAMESPACE!
app_name = 'app'


urlpatterns=[
    url(r'^$',views.map,name='map'),
    url(r'^map/$',views.map,name='map'),
    url(r'^calamity/$',views.calamity,name='calamity'),
    url(r'^provisions/$',views.provisions,name='provisions'),
    url(r'^need/$',views.need,name="need"),
    url(r'^issue/$',views.issue,name='issue'),
]