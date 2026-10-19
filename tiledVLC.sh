#!/bin/bash
# Usage: ./tiledVLC.sh N [directory_path]
# Example: ./tiledVLC.sh 20 /Users/lglab/Public/focused_mp3s/

REQUESTED_N="${1:-20}"
MP3_DIR="${2:-/Users/lglab/Public/focused_mp3s/}"

# 1. Handle N = 0 (Jumps straight to master control loop)
if [ "$REQUESTED_N" -eq 0 ]; then
    echo "N=0 specified. Skipping launch loop, jumping to master controls..."
else
    # Cap N at N_max = 20
    if [ "$REQUESTED_N" -gt 20 ]; then
        N=20
    else
        N="$REQUESTED_N"
    fi

    # 2. Collect, shuffle (using awk for macOS compatibility), and pick N random MP3 files
    if [ ! -d "$MP3_DIR" ]; then
        echo "Error: Directory $MP3_DIR does not exist."
        exit 1
    fi

    # Read files into an array using standard read loop
    ALL_FILES=()
    while IFS= read -r file; do
        [[ -n "$file" ]] && ALL_FILES+=("$file")
    done < <(find "$MP3_DIR" -maxdepth 1 -name "*.mp3" | awk 'BEGIN{srand()}{print rand() "\t" $0}' | sort -n | cut -f2-)

    TOTAL_FILES=${#ALL_FILES[@]}

    if [ "$TOTAL_FILES" -eq 0 ]; then
        echo "Error: No .mp3 files found in $MP3_DIR"
        exit 1
    fi

    # Adjust N if there are fewer than N files available
    if [ "$N" -gt "$TOTAL_FILES" ]; then
        N="$TOTAL_FILES"
    fi

    echo "Launching $N random files out of $TOTAL_FILES total files from $MP3_DIR..."

    # 3. Launch selected files in VLC with Repeat/Loop enabled (--loop)
    for ((i=0; i<N; i++)); do
        /Applications/VLC.app/Contents/MacOS/VLC --loop "${ALL_FILES[$i]}" &
        sleep 0.2
    done

    # 4. Wait for windows to spawn, then tile and arrange them via AppleScript
    sleep 2

osascript <<'EOF'
tell application "System Events"
    set vlcProcesses to every process whose name is "VLC"
    set screenWidth to 1440
    set screenHeight to 900
    
    -- Dynamic grid layout based on number of active windows
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
