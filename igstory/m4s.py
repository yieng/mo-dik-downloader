import requests
from clint.textui import progress

base_path = '/Users/lglab/Downloads/'

import sys
optional_arg = sys.argv

urls = []
paths = []


# get thumbnail urls
with open('urls.txt','r',encoding='utf-8') as f:
    urls = f.readlines()
    
if ('\n' in urls):
    urls.remove('\n')

try:
    with open('title.txt','r',encoding='utf-8') as f:
        titles = f.readlines()
except FileNotFoundError:
    thumbnail_paths = ['/Users/lglab/Downloads/thumbnail_' + str(i) + '.jpg' for i in range(len(urls))]
    paths = thumbnail_paths

# transform titles to safe filenames

if len(optional_arg) == 1:
    T = [t.replace('T','_').replace('.000Z','_UTC').replace(':','-') for t in titles]
titles = T

# finally process the urls and titles

##for url in urls:
##    if 'mp4' in url:
        

urls = [x.replace('\n','') for x in urls]
titles = [x.replace('\n','') for x in titles]
paths = ['/Users/lglab/Downloads/' + title.split('/')[-1] for title in titles]

urls = ["https://vod-adaptive-ak.vimeocdn.com/exp=1730034776~acl=%2F1b332dc2-e6a0-4909-9f2d-f794aac5b5ac%2F%2A~hmac=4496a7a6aa460ecb3cbb6cc830631e24c81c679bf574d038722a8af707ca6a71/1b332dc2-e6a0-4909-9f2d-f794aac5b5ac/v2/remux/avf/459815eb-35f0-4dc4-a7dc-f388cbee0bf9/segment.m4s?pathsig=8c953e4f~OF3eRdt7Ww23IAs4hDb-5GsuMT-6gRpQA5uB9Rb6Gbs&r=dXMtd2VzdDE%3D&sid="+str(i)+"&st=video" for i in range(1,655)]
path = "/Users/lglab/Downloads/Architecture - Week 5 - 28NOV22_video.mp4"

# download with progress bar % visible
for url in urls:
    r = requests.get(url, stream=True)
    path = path #s[urls.index(url)]
    with open(path, 'ab') as f:
        try:
            total_length = int(r.headers.get('content-length'))
        except TypeError:
            total_length = 0
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length//1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()

"""
for url in urls:
    r = requests.get(url)
    path = paths[urls.index(url)]
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1025):
            if chunk:
                f.write(chunk)
        print("DONE: " + path)
"""
