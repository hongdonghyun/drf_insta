import requests
from django.shortcuts import render, redirect

from post.models import Youtube_Video, Post

__all__ = (
    'youtube_search',
    'post_youtube',
)


def youtube_search(request):
    # search list API를 이용해서 동영상만
    # request.GET.get('q')에 데이터가 있을경우
    # request.get을 사용한결과를 변수에 할당하고
    # 해당 변수를 템플릿에서 표시
    q = request.GET.get('q')
    url = 'https://www.googleapis.com/youtube/v3/search'
    if q:
        search_params = {
            'part': 'snippet',
            'key': 'AIzaSyCRItz4Z-0ROw7juJJKonE0VFMa8YTkd00',
            'maxResults': '10',
            'type': 'video',
            'q': q,

        }
        response = requests.get(url, params=search_params)
        videos = []
        result = response.json()
        for item in result['items']:
            video, video_created = Youtube_Video.objects.get_or_create(
                youtube_title=item['snippet']['title'],
                youtube_id=item['id']['videoId'],

            )
            videos.append(video)
        context = {
            'response': response.json(),
            'videos': videos
        }

    else:
        context = {}
    return render(request, 'post/youtube_search.html', context)


def post_youtube(request, youtube_id):
    Post.objects.create(author=request.user, youtube_id=youtube_id)
    return redirect('post:post_list')
