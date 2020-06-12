from googleapiclient.discovery import build
import os
import re
from datetime import timedelta

api_key = os.environ.get('YT_API')

youtube = build('youtube','v3',developerKey = api_key)

nextPageToken = None

mins = re.compile(r'(\d+)M')
secs = re.compile(r'(\d+)S')
hrs = re.compile(r'(\d+)H')

total_secs = 0

while True:
    request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId='PLZoTAELRMXVPBTrWtJkn3wWQxZkmTXGwe',
        maxResults = 50,
        pageToken=nextPageToken
    )


    response = request.execute()
    vid_ids = []
    for i in response['items']:
        vid_ids.append(i['contentDetails']['videoId'])

    vid_request = youtube.videos().list(
        part = 'contentDetails',
        id=','.join(vid_ids)
        )

    vid_response = vid_request.execute()

    

    for item in vid_response['items']:
        duration = item['contentDetails']['duration']

        hours = hrs.search(duration)
        minutes = mins.search(duration)
        seconds = secs.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        vedio_seconds = timedelta(
            hours = hours,
            minutes = minutes,
            seconds = seconds
        ).total_seconds()

        total_secs += vedio_seconds


    nextPageToken = response.get('nextPageToken')

    if not nextPageToken:
        break

total_secs = int(total_secs)

minutes,seconds = divmod(total_secs,60)
hours,minutes = divmod(minutes,60)

print(f'{hours}:{minutes}:{seconds}')