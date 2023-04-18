# $1 = video
# $2 = audio
# $3 = output.mp4

ffmpeg -i "/Users/lglab/Downloads/VIMEO/$1" -i "/Users/lglab/Downloads/VIMEO/$2" -c:v copy -c:a aac "/Users/lglab/Downloads/VIMEO/$3"
