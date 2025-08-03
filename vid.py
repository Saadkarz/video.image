import os
import subprocess
import math

# === CONFIG ===
input_file = "vid.mp4"  # Replace with your video file name
output_basename = "part"          # Base name for output parts
chunk_length_minutes = 20         # Length of each chunk in minutes
# ==============

def get_video_duration(filename):
    result = subprocess.run(
        ["ffmpeg", "-i", filename],
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )
    duration_line = [line for line in result.stderr.split('\n') if "Duration" in line]
    if not duration_line:
        raise ValueError("Couldn't find video duration")
    
    duration_str = duration_line[0].split("Duration:")[1].split(",")[0].strip()
    h, m, s = duration_str.split(":")
    return int(h)*3600 + int(m)*60 + float(s)

def split_video(input_file, chunk_length_sec):
    total_duration = get_video_duration(input_file)
    num_parts = math.ceil(total_duration / chunk_length_sec)

    for i in range(num_parts):
        start_time = i * chunk_length_sec
        output_file = f"{output_basename}_{i+1}.mp4"
        print(f"Creating {output_file}...")

        subprocess.run([
            "ffmpeg",
            "-ss", str(start_time),
            "-i", input_file,
            "-t", str(chunk_length_sec),
            "-c", "copy",
            output_file
        ])

    print("✅ Done splitting video!")

if __name__ == "__main__":
    chunk_length_sec = chunk_length_minutes * 60
    split_video(input_file, chunk_length_sec)
