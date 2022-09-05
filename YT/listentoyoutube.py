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
      print('DOWNLOADING (audio only): '+ yt.title)
      t = yt.streams.filter(only_audio=True)
      t[0].download("./")
      #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
      #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename=t[17:-1])
      print('DONE: '+ yt.title)
      print('====================================')
      #  A = input("press enter to continue...") 
