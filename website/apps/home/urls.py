from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('data', views.data, name='data'),
    path('support', views.support, name='support'),
    path('team', views.team, name='team'),
    path('tech', views.tech, name='tech'),
    path('overview', views.overview, name='overview'),
    path('news', views.news, name='news'),
    path('error', views.error, name='error'),
    path('home_jp', views.home_jp, name='home_jp'),
    path('about_jp', views.about_jp, name='about_jp'),
    path('team_jp', views.team_jp, name='team_jp'),
    path('tech_jp', views.tech_jp, name='tech_jp'),
    path('overview_jp', views.overview_jp, name='overview_jp'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)