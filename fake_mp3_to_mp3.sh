for i in *.mp3; do mv "$i" "$(basename "${i/.mp3}").mp4.mp3"; done
for i in *.mp4.mp3; do ffmpeg -i "$i" -q:a 0 -map a "$(basename "${i/.mp4.mp3}").mp3"; rm "$i";  done;
# mkdir $(date "+%Y-%m-%d--%H-%M-%S")
