# Universal Video Downloader

A simple, standalone command-line application to download videos from WeTV, iQIYI, and hundreds of other supported streaming sites.

## Features
- **Standalone Executable**: No Python installation required! Just double-click the `.exe`.
- **Universal Support**: Powered by `yt-dlp`, supporting hundreds of video platforms out of the box.
- **High Quality**: Automatically grabs the best available video and audio quality.
- **Interactive Console**: Simply run the app and paste your URL.

## How to use
1. Download `Universal_Downloader.exe` from the [Releases](https://github.com/seangritthy/universal-video-downloader/releases) page.
2. Double-click the file to open it.
3. Paste the URL of the video you want to download.
4. The downloaded video will be saved in the same directory as the executable.

## Building from source
If you prefer to run from source:
```bash
pip install yt-dlp pyinstaller
python universal_downloader.py
```
To build your own executable:
```bash
pyinstaller --onefile --name Universal_Downloader universal_downloader.py
```
