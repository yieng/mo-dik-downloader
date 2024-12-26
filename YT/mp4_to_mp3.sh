for i in *.mp4; do ffmpeg -i "$i" -q:a 0 -map a "$(basename "${i/.mp4}").mp3"; rm "$i";  done;
# mkdir $(date "+%Y-%m-%d--%H-%M-%S")
