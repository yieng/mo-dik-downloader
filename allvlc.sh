for ((i=1; i<=$1; i++)); do
    /Applications/VLC.app/Contents/MacOS/VLC &
done

while :; do
    echo "Press ENTER to pause all..."
    read
    killall -STOP VLC
    echo "Press ENTER to resume playing..."
    read
    killall -CONT VLC
done
