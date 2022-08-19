from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category, CommentReply, Profile
from .forms import PostForm, CommentForm, CommentReplyForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import Member


def home(request):
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


# 새 갤러리 생성
def post_new(request):
    if request.method == 'POST' or request.method == "FILES":
        form = PostForm(request.POST, request.FILES)       
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user            # user 추가!
            unfinished.save()
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.body = form.cleaned_data['body']
            # post.author = form.cleaned_data['author']
            # post.category = form.cleaned_data['category']
            # form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form':form})

# 갤러리 상세페이지
def post_detail(request, post_id):
    detail = get_object_or_404(Post, pk=post_id) 
    comment_form = CommentForm()
    comment_reply_form = CommentReplyForm()
    return render(request, 'post_detail.html', {'detail':detail, 'comment_form':comment_form, 'comment_reply_form':comment_reply_form})


# 댓글
def comment_new(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.comment_name = request.user
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

    
    # comment_reply = get_object_or_404(Comment, pk=comment_id)
    # if request.method == "POST":
    #     form = CommentReplyForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.comment_reply = comment_reply
    #         comment.comment_reply_name = request.user
    #         comment.save()
    #         return redirect('post_detail', post_id=comment.comment_reply.post.id)
    # else:
    #     form = CommentReplyForm()
    # return render(request, 'post_detail.html', {'form': form})


    
    # form = CommentReplyForm(request.POST)
    # if form.is_valid():
    #     finished = form.save(commit=False)
    #     finished.comment_reply = get_object_or_404(Comment, pk=comment_id)
    #     finished.comment_reply_name = request.user
    #     finished.save()
        
    # return redirect('post_detail', comment_id=finished.post.id)



# 검색
def search(request):
        keyword = request.POST.get('searched', "") 
        if keyword:
            categories = Post.objects.all()
            posts = categories.filter(category__contains=keyword)
            return render(request, 'searched.html', {'posts':posts, 'keyword':keyword})
        else:
            return render(request, 'searched.html', {})

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
        return HTTPResponse(content_type='appliction/json')

def count_content_view(request, today):
    today = DateFormat(datetime.now()).format('Ymd')
    content = Post.objects.order_by('created')
    content_count = content.exclude(deleted = True).filter(date = today).count()
    context = {
        'newcontent' : content,
        'content_count' : content_count,
    }
    
    return render(request, context=context)