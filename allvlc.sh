# This program opens up multiple VLC instances in the background.
# Use in tmux!
# Usage: ./allvlc.sh x # x is a non-negative integer
for ((i=1; i<=$1; i++)); do
    /Applications/VLC.app/Contents/MacOS/VLC &
done

# The following code helps MASS play/pause all VLC instancs AT ONCE without manual clicking on each.
# Usage: ./allvlc.sh 0 # 0 bypasses the VLC-opening loop entirely and jumps ahead to these controls.
while :; do
    echo "Press ENTER to pause all..."
    read
    killall -STOP VLC
    echo "Press ENTER to resume playing..."
    read
    killall -CONT VLC
done
