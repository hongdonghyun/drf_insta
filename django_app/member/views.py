from django.shortcuts import render, redirect

from member.models import User


def login(request):
    # member/login.html생성
    # username,password,button이 있는 html생성
    # POST요청이 올 경우 로그인 완료 후 post_list이동
    # 실패할 경우 HttpResponse로 Login invalid 띄우기



    if request.method == "POST":
        username = request.POST.get('id', '')
        password = request.POST.get('password', '')
        user = User.objects.create(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('member_login')
    else:
        return render(request, 'member/login.html')
