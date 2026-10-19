from pytubefix import YouTube
from pytubefix.cli import on_progress

"""
yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)
ys = yt.streams.get_audio_only()
ys.download(mp3=True)
"""

import re

# make sure NO non-YouTube links are in the file.
with open('youtube_urls.txt','r+') as f:
   YT = f.readlines()

#YT = sorted(list(set(YT)))
# print(YT)
lenYT = len(YT)
count=0
maxcount=10
j = 0
while (lenYT > 0) and count<maxcount:
   t = YT[j]
   try:
      YouTube(t, on_progress_callback = on_progress)#, use_oauth=False, allow_oauth_cache=False)
   except pytube.exceptions.RegexMatchError or http.client.IncompleteRead: 
      print(t+"  ... TRY AGAIN"+t)
      count+=1
   else:
      yt = YouTube(t)#, use_oauth=True, allow_oauth_cache=True)
      yt_title = yt.title
      print(yt_title)
      print('DOWNLOADING (audio only): ' + yt_title)

      # Standard loading
      try:
         videoid = t.split('v=')[1].split('&index')[0].split('&list')[0].replace('\n','')
      except IndexError or pytube.exceptions.AgeRestrictedError:
         try:
            videoid = t.split('v=')[1].replace('\n','')
         except IndexError or pytube.exceptions.AgeRestrictedError:
            try:
               if 'shorts' in t:
                  videoid = t.split('shorts/')[1].replace('\n','')
               else:
                  videoid = t.split('.be/')[1].replace('\n','')
            except pytube.exceptions.AgeRestrictedError:
               continue
      new_file_name = re.sub(r'[^\w]', '_', yt_title) + '_' + videoid +'.mp4'
      #new_file_name = t.split('v=')[1].replace('\n','')+'.mp4'


      #new_file_name = "./" + re.sub(r'[^\w]', '_', yt_title) + '_' + t.split('=')[1].replace('\n','')+'.mp4'
      #new_file_name = new_file_name.split('&list')[0]
      #new_file_name = new_file_name.split('&t')[0]
      #if '.mp4' not in new_file_name:
      #   new_file_name = new_file_name+'.mp4'

      new_path = '/Users/lglab/Public/clear_all_videos/mp3/'
      new_file_name = new_path+new_file_name
      try:
         ty = yt.streams.filter(only_audio=True, file_extension='mp4')
         #ty[0].download("./") # no YT id
         ty[0].download(filename=new_file_name)
         #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
         #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename=ty[17:-1])
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
      except pytube.exceptions.LiveStreamError: #'''pytube.exceptions.AgeRestrictedError or''' 
         print('— age restrict / livestream error, skip!')
         j=j+1
      print('====================================')
      #  A = input("press enter to continue...") 
      #  A = input("press enter to continue...") 
