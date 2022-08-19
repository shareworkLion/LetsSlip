from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from LsApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('mygallery/', views.mygallery, name='mygallery'),

    # LsApp
    path('', views.home, name='home'), # 유저 페이지
    path('search/', views.search, name='search'),
    path('board/', views.gallery, name='gallery'),
    path('board/write', views.post_new, name='post_new'),
    path('board/write/success', views.gallery_success, name='gallery_success'),
    path('board/detail/<int:post_id>', views.post_detail, name='post_detail'),
    path('comment_new/<int:post_id>', views.comment_new, name='comment_new'),
    path('commentreply/<int:comment_id>', views.commentreply, name='commentreply'),
    path('post_like_toggle/<int:post_id>', views.post_like_toggle, name='post_like_toggle'),
    
    # accounts
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),
    path('signup2/', accounts_views.signup2, name='signup2'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)