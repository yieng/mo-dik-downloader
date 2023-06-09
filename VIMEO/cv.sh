# $1 = video
# $2 = audio
# $3 = output.mp4

ffmpeg -i "$PWD/$1_video.mp4" -i "$PWD/$1_audio.mp4" -c:v copy -c:a aac "$PWD/$1.mp4"
