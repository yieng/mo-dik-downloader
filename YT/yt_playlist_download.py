from pytube import YouTube
import pytube
from pytube import Playlist
import os
import sys
YT_playlist = sys.argv[1]

try:
   Playlist(YT_playlist)
except pytube.exceptions.RegexMatchError or http.client.IncompleteRead:
   print("  ... FIX ERRORS IN PLAYLIST URL & TRY AGAIN")

p = Playlist(YT_playlist)
playlist_folder = p.title
print('Downloading: ' + playlist_folder)
os.mkdir('./'+p.title)
os.chdir(playlist_folder)

for video in p.videos:
   # hi-res
   video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first().download()
   # low-res
   #video.streams.first().download()

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
