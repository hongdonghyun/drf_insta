import requests
from django.shortcuts import render

from post.models import Video

__all__ = (
    'youtube_search',
    'youtube_save',
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
        context = {
            'response': response.json()
        }
        result = response.json()
        for item in result['items']:
            # print(item['id']['videoId'])
            Video.objects.update_or_create(q=q,youtube_id=item['id']['videoId'])

    else:
        context = {}

    return render(request, 'post/youtube_search.html', context)


def youtube_save(request):
    # [1] 검색결과를 DB에 저장하고, 해당내용을 템플릿에서 보여주기!
    # 1. 유튜브 영상을 저장할 class Video(models.Model)생성
    # 2. 검색결과의 videoId를 Video의 youtube_id필드에 저장
    #       해당필드는 unique해야 함
    # 3. 검색결과에서 videoId가 Video의 youtube_id와 일치하는 영상이 이미 있을경우에는 pass,
    #    없을경우 새 Video객체를 만들어 DB에 저장
    # 4. 이후 검색결과가 아닌 자체 DB에서 QuerySet을 만들어 필터링한 결과를 템플릿에서 표시
    videos = Video.objects.all()
    context = {
        'videos' : videos
    }
    return render(request,'post/youtube_save.html',context)