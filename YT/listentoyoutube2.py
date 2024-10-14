from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix import Stream as stream
from pytubefix import exceptions as E

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
      yt = YouTube(t, on_progress_callback = on_progress)
      yt_title = yt.title
      print(yt_title)
      print('DOWNLOADING: '+ yt_title)

      new_file_name = new_path + re.sub(r'[^\w]', '_', yt_title) + '_' + getVideoID(t) +'.mp4'
      old_file_name = old_path + re.sub(r'[^\w]', '_', yt_title) + '_' + getVideoID(t) +'.mp4'

      ys = yt.streams.get_highest_resolution()
      #ys = yt.streams.filter(progressive=True, file_extension='mp4').download(output_path=new_file_name)
      print(ys)
      #print(stream)
      #yd = stream(ys,).download(output_path=new_file_name)
      ys.download(mp3=True,output_path=new_path, filename=re.sub(r'[^\w]', '_', yt_title) + '_' + getVideoID(t))

      print('DONE: '+ yt_title)

      # DELETE the completed item from the original youtube urls txt file
      with open('youtube_urls.txt','w') as f:
         for y in YT:
            if y!=t:
               f.write(y)
            else:
               f.write('')
         del YT[YT.index(t)]
      lenYT -= 1
      
   except E.RegexMatchError:
      print(t+"  ... TRY AGAIN: "+t)
      j+=1
      continue


print('====================================')



"""from pytubefix import YouTube
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
    ys.download(mp3=True)     #,output_path=new_file_name)

    print('DONE: '+ yt_title)

print('====================================')
"""
