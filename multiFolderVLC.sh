#!/bin/bash
# Usage: ./multiFolderVLC.sh FOLDER_NAME [N]
# Example: ./multiFolderVLC.sh lost_items_recover_mp3 1

TARGET_FOLDER="$1"
REQUESTED_N="${2:-20}"
BASE_DIR="/Users/lglab/Public"

# 1. Handle N = 0 (Jumps straight to master control loop)
if [ "$TARGET_FOLDER" = "0" ] || [ "$REQUESTED_N" -eq 0 ]; then
    echo "Jumping straight to master controls..."
else
    if [ -z "$TARGET_FOLDER" ]; then
        echo "Error: Please specify a folder name."
        echo "Example: ./multiFolderVLC.sh lost_items_recover_mp3 1"
        exit 1
    fi

    FULL_DIR="$BASE_DIR/$TARGET_FOLDER"

    if [ ! -d "$FULL_DIR" ]; then
        echo "Error: Directory $FULL_DIR does not exist."
        exit 1
    fi

    # Cap N at N_max = 20
    if [ "$REQUESTED_N" -gt 20 ]; then
        N=20
    else
        N="$REQUESTED_N"
    fi

    # 2. Collect, shuffle (using awk for macOS compatibility), and pick N random MP3 files from the specified folder
    ALL_FILES=()
    while IFS= read -r file; do
        [[ -n "$file" ]] && ALL_FILES+=("$file")
    done < <(find "$FULL_DIR" -maxdepth 1 -name "*.mp3" | awk 'BEGIN{srand()}{print rand() "\t" $0}' | sort -n | cut -f2-)

    TOTAL_FILES=${#ALL_FILES[@]}

    if [ "$TOTAL_FILES" -eq 0 ]; then
        echo "Error: No .mp3 files found in $FULL_DIR"
        exit 1
    fi

    if [ "$N" -gt "$TOTAL_FILES" ]; then
        N="$TOTAL_FILES"
    fi

    echo "Launching $N random files out of $TOTAL_FILES from category: $TARGET_FOLDER..."

    # 3. Launch selected files in VLC with Playlist Repeat enabled (--repeat)
    for ((i=0; i<N; i++)); do
        /Applications/VLC.app/Contents/MacOS/VLC --repeat "${ALL_FILES[$i]}" &
        sleep 0.2
    done

    # 4. Wait for windows to spawn, then tile and arrange them via AppleScript
    sleep 2

osascript <<'EOF'
tell application "System Events"
    set vlcProcesses to every process whose name is "VLC"
    set screenWidth to 1440
    set screenHeight to 900
    
    set winCount to count of vlcProcesses
    if winCount <= 4 then
        set cols to 2
    else if winCount <= 12 then
        set cols to 4
    else
        set cols to 5
    end if
    
    set winWidth to screenWidth div cols
    set winHeight to 110
    
    set index to 0
    tell application "VLC" to activate
    
    repeat with p in vlcProcesses
        try
            tell window 1 of p
                set colIdx to index mod cols
                set rowIdx to index div cols
                set position to {colIdx * winWidth, rowIdx * winHeight}
                set size to {winWidth, winHeight}
            end tell
            set index to index + 1
        end try
    end repeat
end tell
EOF

fi

# 5. Master Play/Pause Control Loop
while :; do
    echo "Press ENTER to pause all..."
    read
    killall -STOP VLC
    echo "Press ENTER to resume playing..."
    read
    killall -CONT VLC
done
