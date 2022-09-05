from bs4 import BeautifulSoup as BS
import requests
import re

from selenium import webdriver # Celente-tium >o<
import time

### GET ALL THE VIDEO URLS

with open('video_list.txt','r') as f:
    many = f.readlines()

#many = sorted(list(set(many)), reverse=True)
if ('\n' in many):
    many.remove('\n')


### BRIGHTEON: GET ALL THE M3U8'S & TITLES
for url in many:
    if 'brighteon.com' in url:
        brighteon = open('brighteon_vlc.sh','w+',encoding='utf-8')
        brighteon.write("/Applications/VLC.app/Contents/MacOS/VLC -vvv ")
    if ('bitchute.com' in url) or ('rumble.com' in url) or ('brandnewtube.com' in url):
        bitchute_rumble = open('bitchute_rumble_bnt.html','w+',encoding='utf-8')
        bitchute_rumble.write("<ol>")
    if "odysee.com" in url:
        odysee = open('odysee_vlc.sh','w+',encoding='utf-8')
        odysee.write("/Applications/VLC.app/Contents/MacOS/VLC -vvv ")
    if "besovereign.com" in url:
        besovereign = open('besovereign_vlc.sh','w+',encoding='utf-8')
        besovereign.write("/Applications/VLC.app/Contents/MacOS/VLC -vvv ")

Srcs = []
Titles = []

for url in many:
    print(url)
    if "brighteon.com" in url:

        page = requests.get(url)
        soup = BS(page.text, 'html.parser')
        print('√')
        
        if (soup.find('source', {'type':'application/x-mpegURL'}) == None):
            continue
        else:
            source = soup.find('source', {'type':'application/x-mpegURL'})
        s = source['src']

        title_original = soup.find('div', {'class':'main-video-title'}).text
        title = re.sub(r'[^\w]', ' ', title_original)
        
        index = s.find('.m3u8')
        src = s[:index] + '_270' + s[index:]

        command = src+' \":sout=#transcode{vcodec=h264,acodec=mp4a,ab=128,channels=2,samplerate=44100,deinterlace}:std{access=file,mux=mp4,dst=\''+title+'.mp4\'}\" '

        brighteon.write(command+' ')
    
    # BITCHUTE

    elif "bitchute.com" in url:

        page = requests.get(url)
        soup = BS(page.text, 'html.parser')
        
        if (soup.find('source', {'type':'video/mp4'}) == None):
            continue
        else:
            source = soup.find('source', {'type':'video/mp4'})
            s = source['src']   

        title_original = soup.find('h1', {'id':'video-title'}).text
        t = re.sub(r'[^\w]', ' ', title_original)

        bitchute_rumble.write("<li>")
        bitchute_rumble.write('<a href="'+s+'" title="'+t+'" download="'+t+'.mp4">'+t+'</a>')
        bitchute_rumble.write("</li>")

        Srcs.append(s)
        Titles.append(t)

    # BrandNewTube
    elif "brandnewtube.com" in url:

        page = requests.get(url)
        soup = BS(page.text, 'html.parser')
        
        if (soup.find('source', {'type':'video/mp4'}) == None):
            continue
        else:
            source = soup.find('source', {'type':'video/mp4'})
            s = source['src']   

        title_original = soup.find('h1', {'itemprop':'title'}).text
        t = re.sub(r'[^\w]', ' ', title_original)

        bitchute_rumble.write("<li>")
        bitchute_rumble.write('<a href="'+s+'" title="'+t+'" download="'+t+'.mp4">'+t+'</a>')
        bitchute_rumble.write("</li>")

        Srcs.append(s)
        Titles.append(t)

    # RUMBLE: requires delayed extraction of HTML source, else no .mp4 found, thus "selenium")
    
    elif "rumble.com" in url:
        
        browser = webdriver.Safari()
        '''
        You must enable the 'Allow Remote Automation' option in Safari's
        Develop menu to control Safari via WebDriver.
        '''

        browser.get(url)
        time.sleep(2)
        
        title_original = browser.execute_script("return document.title")
        t = re.sub(r'[^\w]', ' ', title_original)
        s = browser.execute_script("return document.querySelector('video').src")

        bitchute_rumble.write("<li>")
        bitchute_rumble.write('<a href="'+s+'" title="'+t+'" download="'+t+'.mp4">'+t+'</a>')
        bitchute_rumble.write("</li>")

        browser.close()

        Srcs.append(s)
        Titles.append(t)

    elif "odysee.com" in url:

##        page = requests.get(url)
##        soup = BS(page.text, 'html.parser')
##        print('√')
##        
##        if (soup.find('video', {'class':'vjs-tech'}) == None):
##            continue
##        else:
##            source = soup.find('video', {'class':'vjs-tech'})
##        s = source['src']
##
##        title_original = soup.find('h1', {'class':'card__title'}).text
##        print(title_original)
##        t = re.sub(r'[^\w]', ' ', title_original).replace('  ','_')
##
##        Srcs.append(s)
##        Titles.append(t)

        browser = webdriver.Safari()
        '''
        You must enable the 'Allow Remote Automation' option in Safari's
        Develop menu to control Safari via WebDriver.
        '''

        browser.get(url)
        time.sleep(10)
        
        title_original = browser.execute_script("return document.title")
        title = re.sub(r'[^\w]', ' ', title_original).replace(' ','')
        src = browser.execute_script("return document.querySelector('.vjs-tech').src")
        if ".m3u8" in src:
            command = src+' \":sout=#transcode{vcodec=mp1v,acodec=mpga,ab=128,channels=2,samplerate=44100,deinterlace}:std{access=file,mux=ts,dst=\''+title+'.ts\'}\" '
        else:
            command = src+' \":sout=#transcode{vcodec=h264,acodec=mp4a,ab=128,channels=2,samplerate=44100,deinterlace}:std{access=file,mux=mp4,dst=\''+title+'.mp4\'}\" '

        odysee.write(command+' ')
        browser.close()

    elif "besovereign.com" in url:

        page = requests.get(url)
        soup = BS(page.text, 'html.parser')
        print('√')
        
        if (soup.find('div', {'id':'jwplayer_data_contaioner'}) == None):
            browser = webdriver.Safari()
            browser.get(url)
            title_original = browser.execute_script("return document.querySelector('h4.text-ellipsis').title")
            src = browser.execute_script("return document.querySelector('div#jwplayer_data_contaioner').getAttribute('data-url')")
            browser.close()
        else:
            source = soup.find('div', {'id':'jwplayer_data_contaioner'})
            src = source['data-url'].replace("'","\'")
            title_original = soup.find('h4', {'class':'text-ellipsis'}).text

        title = re.sub(r'[^\w]', ' ', title_original).replace('  ','_')

        command = src+' \":sout=#transcode{vcodec=h264,acodec=mp4a,ab=128,channels=2,samplerate=44100,deinterlace}:std{access=file,mux=mp4,dst=\''+title+'.mp4\'}\" '
        besovereign.write(command+' ')

try:
    brighteon
except NameError:
    print("Brighteon links were not found.")
else:
    print("Brighteon links were found.")
    brighteon.write("\n")
    brighteon.close()

try:
    bitchute_rumble
except NameError:
    print("Bitchute / Rumble / BrandNewTube links were not found.")
else:
    print("Bitchute / Rumble / BrandNewTube links were found.")
    bitchute_rumble.write("</ol>")
    bitchute_rumble.close()
    for i in range(len(Srcs)):
        print('Bitchute / Rumble / BrandNewTube: Downloads Starting...')
        print('>>> '+ Titles[i])
        r = requests.get(Srcs[i])
        with open(Titles[i] + '.mp4', 'wb') as f:
            for chunk in r.iter_content(chunk_size=1025):
                if chunk:
                    f.write(chunk)
        print("DONE: " + Titles[i])

try:
    odysee
except NameError:
    print("Odysee links were not found.")
else:
    print("Odysee links were found.")
    odysee.close()

try:
    besovereign
except NameError:
    print("Besovereign links were not found.")
else:
    print("Besovereign links were found.")
    besovereign.write("\n")
    besovereign.close()
