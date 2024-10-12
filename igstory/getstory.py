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

# download with progress bar % visible
for url in urls:
    r = requests.get(url, stream=True)
    path = paths[urls.index(url)]
    with open(path, 'wb') as f:
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
