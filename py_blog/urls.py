
from django.contrib import admin
from django.urls import path
from blog import views as blog_views
from user_blog import views as blog_views_user



urlpatterns = [
    path('',blog_views.index,name='home'),
    path('login/',blog_views_user.user_login,name='login'),
    path('logout/',blog_views_user.user_logout,name='logout'),
    path('category/<slug:tag_slug>/', blog_views.index, name='cat'),
    path('category/<slug:tag_slug>/<slug:post_slug>/',blog_views.tag_post,name='post'),
    path('admin/', admin.site.urls),
]
