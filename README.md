# Video Splitter

A simple Python script to split large video files into smaller chunks of specified duration using FFmpeg.

## Features

- Split any video file into chunks of configurable length
- Preserves original video and audio quality (no re-encoding)
- Fast processing using stream copy
- Automatic duration detection
- Simple configuration

## Requirements

### Software Dependencies

- **Python 3.6+**
- **FFmpeg** - Must be installed and accessible from command line

### Installing FFmpeg

#### Windows
1. Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extract to a folder (e.g., `C:\ffmpeg`)
3. Add `C:\ffmpeg\bin` to your system PATH environment variable
4. Restart your command prompt/terminal

#### macOS
```bash
# Using Homebrew
brew install ffmpeg
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg
```

## Usage

### Basic Usage

1. Place your video file in the same directory as the script
2. Update the configuration in `vid.py`:
   ```python
   input_file = "your_video.mp4"        # Your video filename
   output_basename = "part"             # Output filename prefix
   chunk_length_minutes = 20            # Length of each chunk in minutes
   ```
3. Run the script:
   ```bash
   python vid.py
   ```

### Configuration Options

| Variable | Description | Default |
|----------|-------------|---------|
| `input_file` | Path to your input video file | `"vid.mp4"` |
| `output_basename` | Prefix for output files | `"part"` |
| `chunk_length_minutes` | Duration of each chunk in minutes | `20` |

### Example

If you have a 90-minute video and set `chunk_length_minutes = 20`, the script will create:
- `part_1.mp4` (20 minutes)
- `part_2.mp4` (20 minutes) 
- `part_3.mp4` (20 minutes)
- `part_4.mp4` (20 minutes)
- `part_5.mp4` (10 minutes)

## How It Works

1. **Duration Detection**: Uses FFmpeg to analyze the input video and extract its total duration
2. **Chunk Calculation**: Calculates how many parts are needed based on the specified chunk length
3. **Video Splitting**: Uses FFmpeg with stream copy (`-c copy`) to split the video without re-encoding
   - This preserves original quality
   - Processing is very fast
   - Both video and audio streams are included

## Supported Formats

The script works with any video format supported by FFmpeg, including:
- MP4
- AVI
- MOV
- MKV
- WebM
- And many more...

## Troubleshooting

### "ffmpeg is not recognized"
- Make sure FFmpeg is installed and added to your system PATH
- Try restarting your terminal/command prompt after installation
- Verify installation: `ffmpeg -version`

### "Couldn't find video duration" 
- Check if your video file exists and is not corrupted
- Ensure the file is a valid video format
- Try with a different video file

### Permission Errors
- Make sure you have write permissions in the output directory
- Check if output files already exist and are not in use

## Technical Details

### FFmpeg Command Used
```bash
ffmpeg -ss <start_time> -i <input_file> -t <duration> -c copy <output_file>
```

- `-ss`: Start time offset
- `-i`: Input file
- `-t`: Duration to extract
- `-c copy`: Copy streams without re-encoding

### Performance
- **Fast**: No re-encoding means processing is limited by disk I/O
- **Quality**: Original quality is preserved
- **File Size**: Output files maintain similar bitrate to original

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## Changelog

### v1.0.0
- Initial release
- Basic video splitting functionality
- FFmpeg integration
- Configurable chunk duration
