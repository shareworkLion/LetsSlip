from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Member


def login(request):
    if request.method == "POST":
        m_id = request.POST['m_id']
        pwd = request.POST['pwd']
        if Member.objects.filter(m_id=m_id).exists():
            getMember = Member.objects.get(m_id = m_id)
            if getMember.pwd == pwd:
                request.session['loginOk'] = True
                request.session['id'] = m_id
                request.session['pwd'] = pwd
                context = {
                    "result" : "로그인 성공"
                }
                return redirect('home')
            else :
                request.session['loginOk'] = False
                context = {
                    "result" : "비밀번호가 틀렸습니다"
            }
        else :
            request.session['loginOk'] = False
            context = {
                "result" : "존재하지 않는 id입니다"
        }
            #return render(request, 'home.html')
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    request.sesseion['loginOk'] = False
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        if request.POST['pwd'] == request.POST['repwd']:
            user = Member.objects.create(         
                     m_id    = request.POST['m_id'],                            
                     nick_nm     = request.POST['nick_nm'],
                     pwd = request.POST['pwd']
                     )
             
            #Member.login(request, user)
            return render(request, 'login.html')
    return render(request, 'join.html')

def signup2(request):
    if request.method == 'POST':
        return render(request, 'login.html')
    return render(request, 'join2.html')