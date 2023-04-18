# $1 = video
# $2 = audio
# $3 = output.mp4

ffmpeg -i "$PWD/$1" -i "$PWD/$2" -c:v copy -c:a aac "$PWD/$3"
