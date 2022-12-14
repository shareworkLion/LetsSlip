# Generated by Django 4.1 on 2022-08-15 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LsApp', '0004_alter_commentreply_comment_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('b_no', models.AutoField(primary_key=True, serialize=False)),
                ('b_name', models.CharField(max_length=255)),
                ('b_img', models.CharField(blank=True, max_length=255, null=True)),
                ('regdate', models.DateTimeField()),
                ('b_intro1', models.CharField(max_length=255)),
                ('b_intro2', models.CharField(max_length=255)),
                ('b_intro3', models.CharField(max_length=255)),
                ('suc_intro1', models.CharField(blank=True, max_length=255, null=True)),
                ('suc_intro2', models.CharField(blank=True, max_length=255, null=True)),
                ('suc_intro3', models.CharField(blank=True, max_length=255, null=True)),
                ('open_yn', models.CharField(blank=True, max_length=1, null=True)),
                ('comment_yn', models.CharField(blank=True, max_length=1, null=True)),
                ('cheerup_yn', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'board',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cheerup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'cheerup',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('k_no', models.AutoField(primary_key=True, serialize=False)),
                ('k_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'keyword',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('m_no', models.AutoField(primary_key=True, serialize=False)),
                ('m_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('pwd', models.CharField(max_length=255)),
                ('nick_nm', models.CharField(max_length=255)),
                ('galary_nm', models.CharField(blank=True, max_length=255, null=True)),
                ('motto', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_img', models.CharField(blank=True, max_length=255, null=True)),
                ('mbti', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('lock_yn', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'member',
                'managed': False,
            },
        ),
    ]
