import requests ,random,json



# YouTube API key
API_KEY = 'AIzaSyDuzxutoocl94tIzUNBxPQxxwg5foqDMaw'



# 获取随机视频列表的函数
def get_random_videos(channel_id):
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={channel_id}&maxResults=50&order=date&type=video&key={API_KEY}'
    response = requests.get(url).json()
    if 'items' not in response:
        return []
    
    videos = response['items']
    random_videos = random.sample(videos, min(10, len(videos)))  # 随机选择10个视频
    video_ids = ','.join([video['id']['videoId'] for video in random_videos])

    # 获取视频的详细信息
    video_details_url = f'https://www.googleapis.com/youtube/v3/videos?part=contentDetails,snippet&id={video_ids}&key={API_KEY}'
    details_response = requests.get(video_details_url).json()


    formatted_data = json.dumps(details_response['items'], indent=4, ensure_ascii=False)
    
    print(formatted_data)
    
    
    

get_random_videos("UCH6Oc4MAJzzmK0SM805ZnjQ")