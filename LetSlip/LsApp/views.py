from time import time
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category, CommentReply, Profile, Board
from .forms import PostForm, CommentForm, CommentReplyForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import Member
from datetime import datetime 
from django.utils.dateformat import DateFormat
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def home(request):
    # count_content_view(request=True, pk=id)
    if request.method == "POST":
        userid = request.POST['userid']
        pwd = request.POST['password']
        user = auth.authenticate(request, userid=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'index.html')


# 유저 갤러리 
def mygallery(request):
    if request.method == "POST":
        if request.session['loginOk'] == True:
            # m_id= request.session['id']
            # pwd= request.session['pwd']
            return render(request, 'join.html')
        else:
            return redirect('login.html')
    else:
        if request.session['loginOk'] == True:
            m_id= request.session['id']
            pwd= request.session['pwd']
            return render(request, 'my_gallery_category.html')
        else:
            return redirect('login.html')

# 일단 이 부분을 본인 갤러리로 두고 구현했음
def gallery(request):
    # gallery = Board.objects.all()
    # post_list = gallery.filter(m_no=request.user.username)
    post_list = Board.objects.all()
    posts = Board.objects.filter().order_by('-regdate')
    paginator = Paginator(posts, 6)
    pagenum = request.GET.get('page')
    posts = paginator.get_page(pagenum)
    return render(request, 'my_gallery_category.html',{'post_list':post_list, 'posts': posts})

def gallery_success(request):
    return render(request, 'join_success.html')

# 새 갤러리 생성
@login_required(login_url='login')
def post_new(request):
    if request.method == 'POST' or request.method == "FILES":
        form = PostForm(request.POST, request.FILES)       
        if form.is_valid():
            post = Board()
            post.s1 = form.cleaned_data['b_intro1']
            post.s2 = form.cleaned_data['b_intro2']
            post.s3 = form.cleaned_data['b_intro3']
            post.c1 = form.cleaned_data['suc_intro1']
            post.c2 = form.cleaned_data['suc_intro2']
            post.c3 = form.cleaned_data['suc_intro3']
            post.name = form.cleaned_data['b_name']
            post.img = form.cleaned_data['b_img']
            post.save()
            return redirect('board')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form':form})


# 갤러리 상세페이지
def post_detail(request, post_id):
    detail = get_object_or_404(Board, pk=post_id) 
    comment_form = CommentForm()
    comment_reply_form = CommentReplyForm()
    return render(request, 'slipComments.html', {'detail':detail, 'comment_form':comment_form, 'comment_reply_form':comment_reply_form})


# 댓글 
@login_required(login_url='login/')
def comment_new(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Board, pk=post_id)
        finished_form.author = request.user
        finished_form.save()
        
    return redirect('post_detail', post_id)


def commentreply(request, comment_id):
    form = CommentReplyForm(request.POST)
    if form.is_valid():
        finished = form.save(commit=False)
        finished.comment_reply = get_object_or_404(Comment, pk=comment_id)
        finished.comment_reply_name = request.user
        finished.save()
        
    return redirect('post_detail', post_id=finished.comment_reply.post.id)



# 검색
def search(request):
        keyword = request.POST.get('searched', "") 
        if keyword:
            categories = Board.objects.all()
            posts = categories.filter(b_name__contains=keyword)
            return render(request, 'search_success.html', {'posts':posts, 'keyword':keyword})
        else:
            return render(request, 'search_success.html', {})


# def detail(request, post_id):
#     context = dict()
#     my_post = get_object_or_404(Post, pk=post_id)

#     context['my_post'] = my_post

#     return render(request, 'detail.html', context)

# 게시글 좋아요 기능
@login_required
def post_like_toggle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user
    profile = Profile.objects.get(user=user)

    try:
        check_like = profile.like_post.get(id=post_id)
        profile.like_post.remove(post)
        post.like_count -= 1
        post.save()
    except:
        profile.like_post.add(post)
        post.like_count += 1
        post.save()

    return redirect('home.html', post_id)


# def likes(request, likes_id):
#     likes_count = PostForm(request.POST)
#     if request.user.is_authenticated:
#         post = get_object_or_404(Post, pk=likes_id)

#         if post.likes.filter(pk=request.user.pk).exists():
#             post.likes.remove(request.user)
#         else:
#             post.likes.add(request.user)
#         return redirect('home', likes_id)
#     return redirect('login')

# 오늘 올라온 게시물의 수
def timesave(request):
    if request.method == 'POST':
        timesave = timesave()
        timesave.save_date = request.POST.get('time')
        timesave.date = DateFormat(datetime.now()).format('Ymd')
        timesave.save()
        return HttpResponse(content_type='appliction/json')

def count_content_view(request, pk):
    today = DateFormat(datetime.now()).format('Ymd')
    content = Post.objects.order_by('created')
    content_count = content.exclude(deleted = True).filter(date = today).count()
    context = {
        'newcontent' : content,
        'content_count' : content_count,
    }
    
    return render(request, context=context)

def aboutUs(request):
    return render(request, 'aboutUs.html')

def my_gallery_category(request):
    return render(request, 'my_gallery_category.html')

def my_gallery_category2(request):
    return render(request, 'my_gallery_category2.html')

def my_gallery_category3(request):
    return render(request, 'my_gallery_category3.html')

def my_gallery_category1_2(request):
    return render(request, 'my_gallery_category1_2.html')

def otherUserSlip(request):
    return render(request, 'otherUserSlip.html')

def slipComments(request):
    return render(request, 'slipComments.html')

def myPage1(request):
    return render(request, 'myPage1.html')

def myPage2(request):
    return render(request, 'myPage2.html')

def myPage3(request):
    return render(request, 'myPage3.html')

def myPage4(request):
    return render(request, 'myPage4.html')

def post(request):
    return render(request, 'post.html')

def mySlip(request):
    return render(request, 'mySlip.html')

def post_success(request):
    return render(request, 'post_success.html')