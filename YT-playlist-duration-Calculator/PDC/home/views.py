from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home/home.html")


def get_time(id):
    from googleapiclient.discovery import build
    import os
    import re
    from datetime import timedelta



    youtube = build('youtube','v3',developerKey = 'AIzaSyDidtk31_vf9nCbcebnuwn9SJjUWb0VHCY')

    nextPageToken = None

    mins = re.compile(r'(\d+)M')
    secs = re.compile(r'(\d+)S')
    hrs = re.compile(r'(\d+)H')

    total_secs = 0

    while True:
        request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=id,
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
    v = response['pageInfo']
    total_vids = v['totalResults']
    return f'The total number of videos :{total_vids} Total time: {hours} Hours:{minutes} Minutes:{seconds} Seconds'


def get_duration(request):
    if request.method == 'POST':
        url = request.POST['url']
        get_id = url.split("=")
        id = get_id[-1]
        try:
            output = get_time(id)
        except:
            output = "Not Found"
    return render(request,'home/home.html',{"output":output})
     
