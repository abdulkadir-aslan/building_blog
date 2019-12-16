
from django.contrib import admin
from django.urls import path
from blog import views as blog_views
from user_blog import views as blog_views_user
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',blog_views.index,name='home'),
    #login
    path('login/',blog_views_user.user_login,name='login'),
    path('logout/',blog_views_user.user_logout,name='logout'),
    path('signup/',blog_views_user.sign_up,name='signup'),
    #list
    path('category/<slug:tag_slug>/', blog_views.index, name='cat'),
    path('category/<slug:tag_slug>/<slug:post_slug>/',blog_views.tag_post,name='post'),
    #Category
    path('cat_added/',blog_views.cat_added,name='cat_added'),
    path('cat_list/',blog_views.cat_list, name='cat_list'),
    path('cat_list/action/<int:cat_id>/<slug:status>/',blog_views.category_update_status,name='cat_delete'),
    #admin
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
