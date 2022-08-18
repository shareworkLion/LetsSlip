from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
#from .models import FollowUser


def login(request):
    if request.method == "POST":
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)
            return render(request, 'login.html')
    return render(request, 'signup.html')

# # 팔로우 기능
# def follow(request, likes_user):
#     if request.user.is_authenticated:
#         person = get_object_or_404(get_user_model())

# def profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             post = Profile()
#             post.nickname = form.cleaned_data['nickname']
#             post.profile_photo = form.cleaned_data['profile_photo']
#             post.gallery_name = form.cleaned_data['gallery_name']
#             post.motto = form.cleaned_data['motto']
#             post.save()
#             return redirect('profile.html')
#         else:
#             form = ProfileForm()
#         return render(request, 'profile.html', {'form':form})

# def profile_update(request):
#     if request.method == 'PUT':
#         return render(request, 'profile_update.html')

# class ProfileView(DetailView):
#     context_object_name = 'profile_user' # model의 User모델에 대한 객체와 로그인한 사용자 명칭과 겹침을 해결
#     model = User
#     template_name = 'accounts/profile.html'

# class ProfileUpDateView(View):
#     def get(self, request):
#         user = get_object_or_404(User, pk=request.user.pk)
#         user_form = UserForm(initial={
#             'nickname':nickname,
#         })

#         if hasattr(user, 'profile'): # user가 profile 가지고 있으면 True
#             profile = user.profile
#             profile_form = ProfileForm(initial={
#                 'profile_photo':profile_photo,
#                 'gallery_name':gallery_name,
#                 'motto':motto,
#             })
#         else:
#             profile_form = ProfileForm()

#         return render(request, 'profile.html', {"user_form":user_form, "profile_form":profile_form})