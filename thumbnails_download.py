import requests
from clint.textui import progress

base_path = '/Users/lglab/Downloads/'

urls = []
paths = []


# get thumbnail urls
with open('thumbnail_list.txt','r',encoding='utf-8') as f:
    urls = f.readlines()
    
if ('\n' in urls):
    urls.remove('\n')

urls = [url.replace('\n','') for url in urls]

thumbnail_paths = ['/Users/lglab/Downloads/thumbnail_' + str(i) + '.jpg' for i in range(len(urls))]
paths = thumbnail_paths


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


