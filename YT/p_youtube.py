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
      yt = YouTube(t, use_oauth=True, allow_oauth_cache=True)
      yt_title = yt.title
      print(yt_title)
      print('DOWNLOADING: '+ yt_title)


      #SUPER LOW RES - for plain music videos
      #yt.streams.first().download()

      # Standard loading
      new_file_name = re.sub(r'[^\w]', '_', yt_title) + '_' + t.split('v=')[1].replace('\n','')+'.mp4'
      #new_file_name = t.split('v=')[1].replace('\n','')+'.mp4'
      yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first().download(filename=new_file_name)
      #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename=new_file_name)

      # HIGH RESOLUTION
      #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

      # HIGH-RES + YouTube video ID
      #new_file_name = re.sub(r'[^\w]', '_', yt_title) + '_' + t.split('=')[1].replace('\n','')+'.mp4'
      #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename=new_file_name)

      '''with open('youtube_title_des.txt','a+') as g:
         g.write(yt_title)
         g.write('\n')
         g.write(str(yt.publish_date))
         g.write('\n')
         g.write(yt.description)
         g.write('\n')'''
      
      print('DONE: '+ yt_title)
      print('====================================')

      # DELETE the completed item from the original youtube urls txt file
      with open('youtube_urls.txt','r+') as f:
         for y in YT:
            if y!=t:
               f.write(y)
      del YT[YT.index(t)]
      #  A = input("press enter to continue...") 
