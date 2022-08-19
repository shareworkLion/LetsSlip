from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from LsApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('mygallery/', views.mygallery, name='mygallery'),

    # LsApp
    path('home/', views.home, name='home'), # 유저 페이지
    path('search/', views.search, name='search'),
    path('board/', views.gallery, name='gallery'),
    path('board/write', views.post_new, name='post_new'),
    path('board/write/success', views.gallery_success, name='gallery_success'),
    path('board/detail/<int:post_id>', views.post_detail, name='post_detail'),
    path('comment_new/<int:post_id>', views.comment_new, name='comment_new'),
    path('commentreply/<int:comment_id>', views.commentreply, name='commentreply'),
    path('post_like_toggle/<int:post_id>', views.post_like_toggle, name='post_like_toggle'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('my_gallery_category/', views.my_gallery_category, name='my_gallery_category'),
    path('my_gallery_category2/', views.my_gallery_category2, name='my_gallery_category2'),
    path('my_gallery_category3/', views.my_gallery_category3, name='my_gallery_category3'),
    path('my_gallery_category1_2/', views.my_gallery_category1_2, name='my_gallery_category1_2'),
    path('otherUserSlip/', views.otherUserSlip, name='otherUserSlip'),
    path('slipComments/', views.slipComments, name='slipComments'),
    path('myPage1/', views.myPage1, name='myPage1'),
    path('myPage2/', views.myPage2, name='myPage2'),
    path('myPage3/', views.myPage3, name='myPage3'),
    path('myPage4/', views.myPage4, name='myPage4'),
    path('post/', views.post, name='post'),

    # accounts
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),
    path('signup2/', accounts_views.signup2, name='signup2'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)