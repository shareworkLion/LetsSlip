from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
import re
from django.utils import timezone


class Board(models.Model):
    b_no = models.AutoField(primary_key=True)
    b_name = models.CharField(max_length=255)
    # b_img = models.CharField(max_length=255, blank=True, null=True)
    b_img = models.ImageField(blank=True, null=True, upload_to='post_photo')
    regdate = models.DateTimeField()
    b_intro1 = models.CharField(max_length=255)
    b_intro2 = models.CharField(max_length=255)
    b_intro3 = models.CharField(max_length=255)
    suc_intro1 = models.CharField(max_length=255, blank=True, null=True)
    suc_intro2 = models.CharField(max_length=255, blank=True, null=True)
    suc_intro3 = models.CharField(max_length=255, blank=True, null=True)
    open_yn = models.CharField(max_length=1, blank=True, null=True)
    comment_yn = models.CharField(max_length=1, blank=True, null=True)
    cheerup_yn = models.CharField(max_length=1, blank=True, null=True)
    m_no = models.ForeignKey('Member', models.DO_NOTHING, db_column='m_no', blank=True, null=True)
    k_no = models.ForeignKey('Keyword', models.DO_NOTHING, db_column='k_no', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board'


class Cheerup(models.Model):
    m_no = models.ForeignKey('Member', models.DO_NOTHING, db_column='m_no', blank=True, null=True)
    b_no = models.ForeignKey(Board, models.DO_NOTHING, db_column='b_no', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cheerup'


class Comment(models.Model):
    c_no = models.AutoField(primary_key=True)
    c_content = models.CharField(max_length=255)
    c_regdate = models.DateTimeField()
    org_c_no = models.IntegerField(blank=True, null=True)
    m_no = models.ForeignKey('Member', models.DO_NOTHING, db_column='m_no', blank=True, null=True)
    b_no = models.ForeignKey(Board, models.DO_NOTHING, db_column='b_no', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class Keyword(models.Model):
    k_no = models.AutoField(primary_key=True)
    k_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'keyword'


class Member(models.Model):
    m_no = models.AutoField(primary_key=True)
    m_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    pwd = models.CharField(max_length=255)
    nick_nm = models.CharField(max_length=255)
    galary_nm = models.CharField(max_length=255, blank=True, null=True)
    motto = models.CharField(max_length=255, blank=True, null=True)
    profile_img = models.CharField(max_length=255, blank=True, null=True)
    mbti = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    lock_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'



category_select = (
    ('취업', '취업'),
    ('직장', '직장'),
    ('공부', '공부'),
    ('학교', '학교'),
    ('시험', '시험'),
    ('알바', '알바'),
    ('일상', '일상'),
    ('관계', '관계'),
    ('웃긴', '웃긴'),
    ('여행', '여행'),
    ('취미', '취미'),
    ('기타', '기타'),
)


class Category(models.Model):
    category_content = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_content


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    like_post = models.ManyToManyField('Post', blank=True, related_name='like_users')

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 
    photo = models.ImageField(blank=True, null=True, upload_to='post_photo')
    category = models.CharField(max_length=20, choices=category_select)
    like_count = models.PositiveIntegerField(default=0) # 응원 기능 위한 변수
    
    class Meta:
        ordering = ['-date']
        
    def __str__(self):
        return self.body

    # def like_count(self):
    #     return self.like_set.count()

# 오류 발생으로 주석 처리함.
# class Comment(models.Model):
#     comment_name = models.ForeignKey(User, on_delete=models.CASCADE)
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.comment
    
class CommentReply(models.Model):
    comment_reply = models.ForeignKey(Comment, on_delete=models.CASCADE)
    comment_reply_name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

# def like_count(self):
#         return self.like_set.count()

# class Like(models.Model):
#     body = models.ForeignKey(Post, on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     create_dt = models.DateTimeField("CREATE DATE", auto_now_add=True, null=True)
         
#     class Meta:
#         unique_together = (("post", "user"),)
#         ordering = ['-create_dt']

# 오늘 게시된 게시물 
class Count(models.Model):
    counts = models.PositiveIntegerField(verbose_name='오늘 올라온 실수들', null=True)