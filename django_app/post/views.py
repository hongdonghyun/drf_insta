from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PostCreateForm, PostModifyForm
from .models import Post, Comment

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

    # 가져오는 과정에서 예외처리를 한다 (Model.DoesNotExist)
    try:
        posts = Post.objects.get(pk=pk)
    except Post.DoesNotExist as e:
        # 1. 404 Notfound를 띄운다
        # 2. redirect로 화면을 되돌린다.
        return HttpResponse('Post not found, detail :{}'.format(e))
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
            post = Post.objects.create(author=user, photo=request.FILES['photo'])

            # post요청시 name이 comment인 input에서 가져옴
            # dict.get
            comment_string = form.cleaned_data['content']
            # 빈 문자열이나 None모두 False로 평가되므로
            # if not으로 댓글로 쓸 내용 또는 comment키가 전달되지 않았음을 검사가능
            if not comment_string == '':
                post.comment_set.create(
                    author=user,
                    post=post,
                    content=comment_string,
                )
            else:
                pass

            return redirect('post_list')

        else:
            context = {
                'form': form
            }
            return render(request, 'post/post_create.html', context)


def post_modify(request, pk):
    post = Post.objects.get(pk=pk)
    comment = Comment.objects.get(pk=pk)
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
            comment.content = form.cleaned_data['content']
            post.save()
            comment.save()
            return redirect('post_detail', pk=post.pk)


def post_delete(request, pk):
    # post_pk에 해당하는 Post에 대한 delete요청만을 받음
    # 처리완료후에는 post_list페이지로 redirect
    post = Post.objects.get(pk=pk)
    comment = Comment.objects.get(pk=pk)
    post.delete()
    return redirect('post_list')





