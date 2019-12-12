
from django.contrib import admin
from django.urls import path
from blog import views as blog_views

urlpatterns = [
    path('',blog_views.index),
    path('category/<slug:cat_slug>/', blog_views.category, name='cat'),
    path('admin/', admin.site.urls),
]
