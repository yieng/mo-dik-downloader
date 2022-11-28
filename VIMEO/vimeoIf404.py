from vimeo_downloader import Vimeo
import re

import pprint
pp = pprint.PrettyPrinter(indent=2)
px = pp.pprint

import requests
from clint.textui import progress

# make sure NO non-YouTube links are in the file.
with open('vimeo_urls.txt','r+') as f:
   VM = f.readlines()

with open('vimeo_titles.txt','r+') as f:
   Titles = f.readlines()

#VM = sorted(list(set(VM)))
# print(YT)

for i in range(len(VM)):
   v = Vimeo(VM[i].replace('\n',''))
   print(v)
   #meta = v.metadata
   #print(meta.title)

   #title = i[-9:-1]
   title = Titles[i][0:-1]

   #v = Vimeo.from_video_id(video_id=i.split('/')[3])
   '''
   v1 = v.__repr__()
   v2 = v._extractor()
   v3 = v._validate_url()
   print(v2)
   '''
   #title = i[-10:-1]
   #title = re.sub(r'[^\w]', ' ', meta.title).replace(' ','')
   s = v.streams

   if len(s)>0:
      # this gives the lowest resolution
      best_stream = s[0]
      
      # this gives the highest resolution
      #best_stream = s[-1]
      
      best_stream.download(download_directory='/Users/lglab/Downloads/VIMEO/',filename=title+'.mp4')
   else:
      vimeo_src = v._extractor()
      
      url = vimeo_src['request']['files']['dash']['cdns']['akfire_interconnect_quic']['url']
      url_base = url.split('/sep/')

      # audio: the second option given
      audio_file = url_base[0] + '/parcel/audio/' + url_base[1].split('/audio/')[1].split(',')[1] + '.mp4'
      
      # video: need to choose resolution
      # sort stream from lowest to highest resolution
      streams = vimeo_src['request']['files']['dash']['streams']
      streams = sorted(streams, key=lambda x: int(x['quality'][0:-1]))
      
      # get the 'id' for video download (not 'profile')
      vid = [(s['quality'], s['id'].split('-')[0]) for s in streams]
      #px(vid)
      
      # this gives the lowest resolution
      vid_choice = vid[0][1]
      
      # this gives the highest resolution
      #vid_choice = s[-1][1]

      # this gives 360p
      #req_res = '360p'
      #vid_choice = [x[1] for x in vid if x[0]==req_res][0]
      # choices: 240p, 360p, 540p, 720p, 1080p, 1440p, 2160p

      video_file = url_base[0] + '/parcel/video/' + vid_choice + '.mp4'

      urls = [audio_file, video_file]
      paths = [title + "_audio.mp4", title + "_video.mp4"]

      # download with progress bar % visible
      for url in urls:
          r = requests.get(url, stream=True)
          path = paths[urls.index(url)]
          with open(path, 'wb') as f:
              total_length = int(r.headers.get('content-length'))
              for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length//1024) + 1): 
                  if chunk:
                      f.write(chunk)
                      f.flush()

#  A = input("press enter to continue...")


