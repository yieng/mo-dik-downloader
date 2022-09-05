from pytube import YouTube
import pytube

# make sure NO non-YouTube links are in the file.
with open('youtube_urls.txt','r+') as f:
   YT = f.readlines()

#YT = sorted(list(set(YT)))
# print(YT)

for t in YT:
   try:
      YouTube(t)
   except pytube.exceptions.RegexMatchError or http.client.IncompleteRead: 
      print(t+"  ... TRY AGAIN"+t)
   else:
      yt = YouTube(t)
      print(yt.title)
      print('DOWNLOADING: '+ yt.title)

      #SUPER LOW RES - for plain music videos
      #yt.streams.first().download()

      # Standard loading
      yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first().download()

      # HIGH RESOLUTION
      #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

      # HI-RES + YouTube video ID
      #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename=t[17:-1])

      print('DONE: '+ yt.title)
      print('====================================')
      #  A = input("press enter to continue...") 
