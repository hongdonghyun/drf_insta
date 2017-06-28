import requests
from googleapiclient.discovery import build


def search_original(q):
    url_api_search = 'https://www.googleapis.com/youtube/v3/search'
    search_params = {
        'part': 'snippet',
        'key': 'AIzaSyACCLlnn_hlOpNk5XUBpRqs-iZWpbTm-J4',
        'maxResults': '10',
        'type': 'video',
        'q': q,
    }
    response = (requests.get(url_api_search, params=search_params)).json()
    return response


DEVELOPER_KEY = "AIzaSyACCLlnn_hlOpNk5XUBpRqs-iZWpbTm-J4"
YOUTUBE_API_SERVICE_NAME = "https://www.googleapis.com/"
YOUTUBE_API_VERSION = "v3"


def search(q):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=q,
        part="id,snippet",
        maxResults=10,
        type='video'
    ).execute()
    return search_response
