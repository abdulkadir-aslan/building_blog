
from django.contrib import admin
from django.urls import path
from blog import views as blog_views

urlpatterns = [
    path('',blog_views.index,name='home'),
    path('category/<slug:tag_slug>/', blog_views.index, name='cat'),
    path('category/<slug:tag_slug>/<slug:post_slug>/',blog_views.tag_post,name='post'),
    path('admin/', admin.site.urls),
]
