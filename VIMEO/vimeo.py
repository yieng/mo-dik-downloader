from vimeo_downloader import Vimeo
import re

# make sure NO non-YouTube links are in the file.
with open('vimeo_urls.txt','r+') as f:
   VM = f.readlines()

#VM = sorted(list(set(VM)))
# print(YT)

for i in VM:
   v = Vimeo(i.replace('\n',''))
   #print(v)
   meta = v.metadata
   print(meta.title)
   #title = i[-9:-1]

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

   # this gives the lowest resolution
   best_stream = s[0] 
   # this gives the highest resolution
   #best_stream = s[-1] 
   best_stream.download(download_directory='/Users/lglab/Downloads/VIMEO/',filename=title+'.mp4')
#  A = input("press enter to continue...")


