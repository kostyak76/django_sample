from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^index|index.html$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
]
