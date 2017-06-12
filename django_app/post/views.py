from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PostCreateForm, PostModifyForm
from .models import Post

User = get_user_model()


def post_list(request):
    # 모든 Post목록을 'posts'라는 key로 context에 담아 return render처리
    # post/post_list.html을 template으로 사용하도록 한다

    # 각 포스트에 대해 최대 4개까지의 댓글을 보여주도록 템플릿에 설정
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'post/post_list.html', context)


def post_detail(request, pk):
    # post_pk에 해당하는 Post객체를 리턴,보여줌
    posts = Post.objects.get(pk=pk)
    context = {
        'post': posts
    }
    return render(request, 'post/post_detail.html', context)


def post_create(request):
    # POST요청을 받아 Post객체를 생성 후 post_list페이지로 redirect
    if request.method == 'GET':
        form = PostCreateForm()
        context = {
            'form': form,
        }
        return render(request, 'post/post_create.html', context)
    elif request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            user = User.objects.first()
            Post.objects.create(author=user, photo=request.FILES['photo'])
            return redirect('post_list')
        else:
            context = {
                'form': form
            }
            return render(request, 'post/post_create.html', context)


def post_modify(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'GET':
        form = PostModifyForm()
        context = {
            'form': form,
            'post': post,
        }
        return render(request, 'post/post_create.html', context)
    elif request.method == 'POST':
        form = PostModifyForm(request.POST, request.FILES)
        if form.is_valid():
            post.photo = request.FILES['photo']
            post.save()
            return redirect('post_detail', pk=post.pk)


def post_delete(request, post_pk):
    # post_pk에 해당하는 Post에 대한 delete요청만을 받음
    # 처리완료후에는 post_list페이지로 redirect
    pass


def comment_create(request, posk_pk):
    # POST요청을 받아 Comment객체를 생성 후 post_detail페이지로 redirect
    pass


def comment_delete(request, posk_pk, comment):
    # POST요청을 받아 Comment객체를 delete, 이후 post_detail페이지로 redirect
    pass
