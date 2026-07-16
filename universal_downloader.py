import sys
import os
import yt_dlp
import tkinter as tk
from tkinter import filedialog

def choose_directory():
    """Opens a folder selection dialog and returns the selected path."""
    root = tk.Tk()
    root.withdraw() # Hide the main tkinter window
    # Ensure it appears on top
    root.attributes('-topmost', True)
    
    print("\nPlease choose a folder to save your video in the popup dialog...")
    folder_path = filedialog.askdirectory(title="Select Save Folder")
    return folder_path

def download_video(url, save_dir):
    """
    Downloads a video from WeTV, iQIYI, and many other supported sites using yt-dlp.
    """
    # The outtmpl requires yt-dlp to output to that specific folder.
    out_path = os.path.join(save_dir, '%(title).100s.%(ext)s')

    ydl_opts = {
        # Force yt-dlp to download the best video and best audio separately and merge them if possible
        'format': 'bestvideo+bestaudio/best',
        # Prioritize H.264 (AVC) video codecs so it works in video editors like Premiere/CapCut without HEVC issues
        'format_sort': ['vcodec:h264', 'res', 'acodec:m4a'],
        # Merge into mp4 container
        'merge_output_format': 'mp4',
        'outtmpl': out_path,
        'restrictfilenames': True,
        'windowsfilenames': True,
        'progress_hooks': [progress_hook],
        'quiet': False, 
        'no_warnings': True
    }
    
    # If bundled via PyInstaller, tell yt-dlp where to find ffmpeg
    if hasattr(sys, '_MEIPASS'):
        ydl_opts['ffmpeg_location'] = sys._MEIPASS

    print(f"\nStarting download for: {url}")
    print(f"Saving to: {save_dir}")
    print("-" * 50)
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n\nDownload completed successfully!")
    except Exception as e:
        print(f"\n\nAn error occurred during download: {e}")

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A').strip()
        speed = d.get('_speed_str', 'N/A').strip()
        eta = d.get('_eta_str', 'N/A').strip()
        # Overwrite the current line with progress
        sys.stdout.write(f"\rDownloading... {percent} | Speed: {speed} | ETA: {eta}")
        sys.stdout.flush()
    elif d['status'] == 'finished':
        print("\nDownload finished, finalizing file...")

if __name__ == "__main__":
    print("Welcome to the Universal Video Downloader (WeTV, iQIYI, etc)!")
    
    # Check if a URL was passed via command line
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Please paste your video URL: ").strip()
        
    if url:
        save_dir = choose_directory()
        if save_dir:
            download_video(url, save_dir)
        else:
            print("No folder selected. Download cancelled.")
    
    # Pause so the console window doesn't immediately close
    input("\nPress Enter to exit...")
