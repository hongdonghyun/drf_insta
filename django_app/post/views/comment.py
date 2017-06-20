from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.http import require_POST

from post.forms import CommentForm
from post.models import Post

User = get_user_model()

__all__ =(
    'comment_create',
    'comment_delete',
    'comment_modify',
)

@require_POST
@login_required
def comment_create(request, post_pk):
    # POST요청을 받아 Comment객체를 생성 후 post_detail페이지로 redirect
    post = get_object_or_404(Post, pk=post_pk)
    print('실행됨')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            print('여기도 실행')
            form.save(post=post, author=request.user)
            return redirect('post:post_detail', post_pk=post.pk)


def comment_modify(request, post_pk):
    # 수정
    pass


def comment_delete(request, post_pk, comment_pk):
    # POST요청을 받아 Comment객체를 delete, 이후 post_detail페이지로 redirect
    pass
