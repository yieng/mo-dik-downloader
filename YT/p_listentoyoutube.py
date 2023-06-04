from pytube import YouTube
import pytube
import re

# make sure NO non-YouTube links are in the file.
with open('youtube_urls.txt','r+') as f:
   YT = f.readlines()

#YT = sorted(list(set(YT)))
# print(YT)
lenYT = len(YT)

while lenYT > 0:
   j = 0
   t = YT[j]
   try:
      YouTube(t)
   except pytube.exceptions.RegexMatchError or http.client.IncompleteRead: 
      print(t+"  ... TRY AGAIN"+t)
   else:
      yt = YouTube(t)#, use_oauth=True, allow_oauth_cache=True)
      yt_title = yt.title
      print(yt_title)
      print('DOWNLOADING (audio only): ' + yt_title)

      new_file_name = "./" + re.sub(r'[^\w]', '_', yt_title) + '_' + t.split('=')[1].replace('\n','')+'.mp4'
      new_file_name = new_file_name.split('&list')[0]
      new_file_name = new_file_name.split('&t')[0]
      if '.mp4' not in new_file_name:
         new_file_name = new_file_name+'.mp4'
      
      ty = yt.streams.filter(only_audio=True, file_extension='mp4')
      #ty[0].download("./") # no YT id
      ty[0].download(filename=new_file_name)
      #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
      #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename=ty[17:-1])
      print('DONE: '+ yt_title)
      print('====================================')
      #  A = input("press enter to continue...") 

      # DELETE the completed item from the original youtube urls txt file
      with open('youtube_urls.txt','w') as f:
         for y in YT:
            if y!=t:
               f.write(y)
            else:
               f.write('')
         del YT[YT.index(t)]
      lenYT -= 1
      #  A = input("press enter to continue...") 
