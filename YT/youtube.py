from pytube import YouTube
import pytube
import re

# make sure NO non-YouTube links are in the file.
with open('youtube_urls.txt','r+') as f:
   YT = f.readlines()

#g = open('youtube_title_des.txt','w+')
#g.close()

#YT = sorted(list(set(YT)))
# print(YT)

for t in YT:
   try:
      YouTube(t)
   except pytube.exceptions.RegexMatchError or http.client.IncompleteRead: 
      print(t+"  ... TRY AGAIN"+t)
   else:
      yt = YouTube(t)
      yt_title = yt.title
      print(yt_title)
      print('DOWNLOADING: '+ yt_title)

      #SUPER LOW RES - for plain music videos
      #yt.streams.first().download()

      # Standard loading
      yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first().download()

      # HIGH RESOLUTION
      #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

      # HI-RES + YouTube video ID
      #new_file_name = re.sub(r'[^\w]', '_', yt_title) + '_' + t.split('=')[1].replace('\n','')+'.mp4'
      #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first().download(filename=new_file_name)

      '''with open('youtube_title_des.txt','a+') as g:
         g.write(yt_title)
         g.write('\n')
         g.write(str(yt.publish_date))
         g.write('\n')
         g.write(yt.description)
         g.write('\n')'''
         
      print('DONE: '+ yt_title)
      print('====================================')
      #  A = input("press enter to continue...") 
