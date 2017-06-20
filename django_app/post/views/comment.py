from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from post.decorators import comment_owner
from ..forms import CommentForm
from ..models import Post, Comment

__all__ = (
    'comment_create',
    'comment_modify',
    'comment_delete',
)


@require_POST
@login_required
def comment_create(request, post_pk):
    # URL에 전달되어온 post_pk로 특정 Post객체 가져옴
    post = get_object_or_404(Post, pk=post_pk)
    # URL의 GET parameter의 'next'값을 가져옴
    next = request.GET.get('next')
    # CommentForm data binding
    form = CommentForm(request.POST)

    # form이 유효할 경우, Comment생성
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    # form이 유효하지 않을 경우, 현재 request에 error메시지 추가
    else:
        result = '<br>'.join(['<br>'.join(v) for v in form.errors.values()])
        messages.error(request, result)
    # next값이 존재하면 해당 주소로, 없으면 post_detail로 이동
    if next:
        return redirect(next)
    return redirect('post:post_detail', post_pk=post.pk)
@comment_owner
@login_required
def comment_modify(request, comment_pk):
    # 수정
    # CommentForm을 만들어서 해당 ModelForm안에서 생성/수정가능하도록 사용
    next = request.GET.get('next')
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'POST':
        form = CommentForm(data=request.POST,instance=comment)
        form.save()
        if next:
            return redirect(next)
        return redirect('post:post_detail',post_pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    context = {
        'form': form,
    }
    return render(request, 'post/comment_modify.html', context)

@comment_owner
@require_POST
@login_required
def comment_delete(request, post_pk, comment_pk):
    # POST요청을 받아 Comment객체를 delete, 이후 post_detail페이지로 redirect
    # comment_delete후에 원래 페이지로 돌아갈 수 있도록 처리
    # ( post_list에서 삭제하면 해당 리스트의 post위치로)
    comment = get_object_or_404(Comment,pk=comment_pk)
    post = comment.post
    comment.delete()
    return redirect('post:post_detail',post_pk=post.pk)
