from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.db import models
from django.views.generic.detail import DetailView
from .models import Work

urlpatterns = [
	path('', views.empty, name='empty'),
   	path('main/', views.main, name='main'),
	path('about/', views.about, name='about'),
	path('designers/', views.designers, name='designers'),
	path('price/', views.price, name='price'),
	path('contacts/', views.contacts, name='contacts'),
	#path(r'^work/(?P<pk>[0-9]+)/$', DetailView.as_view(
#context_object_name="work",
#model=Work,
#template_name="main.html"
#), name='work-detail'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)