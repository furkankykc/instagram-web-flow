from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
                  url(r'^$', views.index, name='home'),
                  url(r'^register$', views.registerInstagram, name='register'),
                  url(r'^dashboard$', views.dashboard, name='dashboard'),
                  url(r'^account/(?P<username>\w+)/$', views.myprofileview, name="detail_profile"),
                  url(r'^account/update/(?P<username>\w+)/$', views.updateAccount, name="update"),
                  # url(r'^account/upload/(?P<username>\w+)/$', views.upload, name="upload"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
