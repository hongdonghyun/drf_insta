import requests
from django.shortcuts import render

__all__ = (
    'youtube_search',
)


def youtube_search(request):
    # search list API를 이용해서 동영상만
    # request.GET.get('q')에 데이터가 있을경우
    # request.get을 사용한 결과를 변수에 할당하고
    # 해당 변수를 템플릿에서 표시

    #검색 결과를
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
    else:
        context = {}

    return render(request, 'post/youtube_search.html', context)
