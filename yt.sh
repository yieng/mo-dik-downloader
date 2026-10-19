#vi Downloads/YT/youtube_urls.txt 
#cd Downloads/YT; python3 youtube.py; cd ~

# $1 can take the value of y=video ot l=audio

#cd ~/Public/clear_all_videos
#mkdir ./mp3/

cd ~/Downloads/YT
vi youtube_urls.txt
python3 $1*4.py 

#if (('l' == $1)); then
#   for file in *.mp4; do ffmpeg -y  -i "$file" "${file%.mp4}.mp3"; rm "$file"; done
#fi
cd ~
