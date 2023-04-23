from pytube import YouTube
import pytube
from pytube import Playlist
import os
import sys
YT_playlist = sys.argv[1]

# make sure NO non-YouTube links are in the file.
#with open('youtube_urls.txt','r+') as f:
#   YT = f.readlines()

# Target: https://youtube.com/playlist?list=PLgWq3ErMFBwTEbdOcsGNcQ1-Cun95NLWD
#YT_playlist = [t for t in YT if 'playlist' in t]


# Mae Brussell
#YT_playlist = 'https://youtube.com/playlist?list=PLgWq3ErMFBwTEbdOcsGNcQ1-Cun95NLWD'

# Dance Playlist #KK
#YT_playlist = 'https://www.youtube.com/playlist?list=PL9tgfl8l0s1nGwRrJobWqeMHbXTa_a-OT'

# energetic songs curated by LYC
#YT_playlist = 'https://www.youtube.com/playlist?list=PLr1lpdmlRU9mrLrxJzBqh7ypee6EiadGD'

# Sam hui english
#YT_playlist = 'https://www.youtube.com/playlist?list=PLzqSRCWQLc9dHwyAnY0JJfaBZAz-n51iy'

try:
   Playlist(YT_playlist)
except pytube.exceptions.RegexMatchError or http.client.IncompleteRead:
   print("  ... FIX ERRORS IN PLAYLIST URL & TRY AGAIN")

p = Playlist(YT_playlist)
playlist_folder = p.title
print('Downloading: ' + playlist_folder)
try:
   os.mkdir('./'+p.title)
except FileExistsError:
   print("Folder exists. Overwriting...")
os.chdir(playlist_folder)

for video in p.videos:
   try:
      # hi-res
      #video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first().download()
      # low-res
      video.streams.first().download()
   except KeyError:
      continue

#YT = sorted(list(set(YT)))
# print(YT)

##for t in YT:
##   try:
##      YouTube(t)
##   except pytube.exceptions.RegexMatchError or http.client.IncompleteRead: 
##      print(t+"  ... TRY AGAIN"+t)
##   else:
##      yt = YouTube(t)
##      print(yt.title)
##      print('DOWNLOADING: '+ yt.title)
##      yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first().download()
##      #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
##      #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename=t[17:-1])
##      print('DONE: '+ yt.title)
##      print('====================================')
##      #  A = input("press enter to continue...") 
##
