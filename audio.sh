#!/bin/bash

echo "Starting MP4 to MP3 conversion and cleanup..."
echo "===================================="

for i in *.mp4; do
    # Skip if no .mp4 files exist in the directory
    [ -e "$i" ] || continue
    
    output_mp3="$(basename "${i/.mp4}").mp3"
    
    echo "Converting: $i -> $output_mp3"
    
    # Run ffmpeg conversion
    ffmpeg -y -i "$i" -q:a 0 -map a "$output_mp3"
    
    # Check if conversion was successful (exit code 0) before deleting original
    if [ $? -eq 0 ]; then
        echo "Conversion successful. Deleting original: $i"
        rm "$i"
    else
        echo "Error: ffmpeg failed on $i. Keeping original file."
    fi
    
    echo "------------------------------------"
done

echo "All tasks completed!"
