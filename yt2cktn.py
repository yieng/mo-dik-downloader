import requests
from clint.textui import progress

from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix import Stream as stream
from pytubefix import exceptions as E

import re


# make sure NO non-YouTube links are in the file.
with open('yt2cktn.txt','r+') as f:
   YT = f.readlines()

lenYT = len(YT)
count=0
maxcount=10
j = 0

new_path = '/Volumes/Elements_2/el_vedado/charlie_kirk_other_channels_yt_pre2019_thumbnails'
old_path = '/Users/lglab/Downloads/YT/'

def getVideoID(t):
   t = t.replace('\n','')
   params = t.split('?')[-1].split('&')
   be = t.split('.be/')[-1]
   shorts = t.split('shorts/')[-1]
   for p in params:
     if 'v=' in p:
         video = p.replace('\n','').replace('v=','')
   abbr = ['.be/','shorts/','live/']
   for a in abbr:
     if a in t:
         video = t.split(a)[-1]
         video = video.split('?')[0]
   print(video)
   #yt_web = "https://www.youtube.com/watch?v="
   #videoid = yt_web + video
   """videoid = t.split('v=')[1].split('&index')[0].split('&list')[0].replace('\n','')
   videoid = t.split('v=')[1].replace('\n','')
   if 'shorts' in t:
     videoid = t.split('shorts/')[1].replace('\n','')
   else:
     videoid = t.split('.be/')[1].replace('\n','')"""
   return video

while (lenYT > 0) and count<maxcount:
   t = YT[j]

   try:
      yt = YouTube(t, 'ANDROID', on_progress_callback = on_progress)
      yt_title = yt.title
      url = yt.thumbnail_url
      print(yt_title)
      print('DOWNLOADING: '+ yt_title)

      r = requests.get(url, stream=True)
      path = new_path + '/' + re.sub(r'[^\w]', '_', yt_title) + '_' + getVideoID(t) +'.jpg'
      with open(path, 'wb') as f:
        try:
            total_length = int(r.headers.get('content-length'))
        except TypeError:
            total_length = 0
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length//1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()

      #new_file_name = new_path + re.sub(r'[^\w]', '_', yt_title) + '_' + getVideoID(t) +'.mp4'
      #old_file_name = old_path + re.sub(r'[^\w]', '_', yt_title) + '_' + getVideoID(t) +'.mp4'

      #ys = yt.streams.get_highest_resolution()
      #ys = yt.streams.filter(progressive=True, file_extension='mp4').download(output_path=new_file_name)
      #print(ys)
      #print(stream)
      #yd = stream(ys,).download(output_path=new_file_name)
      #ys.download(output_path=new_path, filename=re.sub(r'[^\w]', '_', yt_title) + '_' + getVideoID(t) +'.mp4')

      print('DONE: '+ yt_title)
      print('====================================')
      # DELETE the completed item from the original youtube urls txt file
      with open('yt2cktn.txt','w') as f:
         for y in YT:
            if y!=t:
               f.write(y)
            else:
               f.write('')
         del YT[YT.index(t)]
      lenYT -= 1
      
   except E.RegexMatchError:
      print(t+"  ... TRY AGAIN: "+t)
      print('====================================')
      j+=1
      lenYT -= 1
      continue
   #except E.VideoUnavailable:
   #   print(t+": video unavailable")
   #   print('====================================')
   #   j+=1
   #   lenYT -= 1
   #   continue


print('====================================')

