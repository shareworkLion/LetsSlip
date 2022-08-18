from django.db import models


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