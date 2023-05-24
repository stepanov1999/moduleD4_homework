from django.contrib import admin
from django.urls import path, include
from newspaper import views
from newspaper.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('newspaper.urls')),
    path('news/search/', PostsSearch.as_view(), name='search'),
    path('news/add/', PostsAdd.as_view(), name='add'),
    path('news/<int:pk>/edit/', PostEdit.as_view(), name='edit'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='delete'),
    path('', views.home, name='home'),
]

