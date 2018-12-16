from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

from .api.views import index_view

urlpatterns = [

    path('', index_view, name='index'),

    url('', include('backend.api.urls')),

    path('admin/', admin.site.urls),
]
