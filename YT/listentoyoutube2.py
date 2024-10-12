from pytubefix import YouTube
from pytubefix.cli import on_progress

import re

# make sure NO non-YouTube links are in the file.
with open('youtube_urls.txt','r+') as f:
   YT = f.readlines()

lenYT = len(YT)
count=0
maxcount=10
j = 0

new_path = '/Users/lglab/Public/clear_all_videos/'
old_path = '/Users/lglab/Downloads/YT/'

def getVideoID(t):
    videoid = t.split('v=')[1].split('&index')[0].split('&list')[0].replace('\n','')
    videoid = t.split('v=')[1].replace('\n','')
    if 'shorts' in t:
        videoid = t.split('shorts/')[1].replace('\n','')
    else:
        videoid = t.split('.be/')[1].replace('\n','')
    return videoid

while (lenYT > 0) and count<maxcount:
    t = YT[j]
 
    yt = YouTube(t, on_progress_callback = on_progress)
    yt_title = yt.title
    print(yt_title)
    print('DOWNLOADING: '+ yt_title)

    new_file_name = new_path + re.sub(r'[^\w]', '_', yt_title) + '_' + getVideoID(t) +'.mp3'
    old_file_name = old_path + re.sub(r'[^\w]', '_', yt_title) + '_' + getVideoID(t) +'.mp3'
     
    ys = yt.streams.get_audio_only()
    ys.download(mp3=True,output_path=new_file_name)

    print('DONE: '+ yt_title)

print('====================================')

