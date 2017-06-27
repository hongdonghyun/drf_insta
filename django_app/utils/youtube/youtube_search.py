import requests
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


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


def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results,
        type='video'
    ).execute()

    try:
        youtube_search(args)
    except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))


