
from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name':'login.html'},name='login'),
    url(r'^signup/$', views.signup, name='signup'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)