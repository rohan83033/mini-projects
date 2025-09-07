import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys

def download_video(url, save_path):
    try:
        # Configure yt-dlp options for best compatibility
        ydl_opts = {
            'format': 'best[height<=720][ext=mp4]/best[ext=mp4]/best',  # Prefer 720p MP4, fallback to best available
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'noplaylist': True,  # Download single video, not playlist
        }
        
        print("Extracting video information...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # First, get video info
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'Unknown')
            duration = info.get('duration', 0)
            
            print(f"Title: {title}")
            print(f"Duration: {duration // 60}:{duration % 60:02d}")
            
            # Ask for confirmation
            proceed = input(f"\nDownload '{title}'? (y/n): ").lower().strip()
            if proceed in ['y', 'yes']:
                print("Starting download...")
                ydl.download([url])
                print("✅ Video downloaded successfully!")
                return True
            else:
                print("Download cancelled.")
                return False
                
    except yt_dlp.utils.DownloadError as e:
        print(f"❌ Download error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def download_with_gui(url, save_path):
    """GUI version with messagebox feedback"""
    try:
        ydl_opts = {
            'format': 'best[height<=720][ext=mp4]/best[ext=mp4]/best',
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'noplaylist': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'Unknown')
            
            # Show confirmation dialog
            result = messagebox.askyesno("Confirm Download", 
                                       f"Download video:\n{title}?")
            if result:
                ydl.download([url])
                messagebox.showinfo("Success", "Video downloaded successfully!")
                return True
            else:
                messagebox.showinfo("Cancelled", "Download cancelled.")
                return False
                
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video:\n{str(e)}")
        return False

def open_file_dialog():
    folder = filedialog.askdirectory(title="Select Download Folder")
    if folder:
        print(f"Selected folder: {folder}")
    return folder

def validate_url(url):
    """Basic URL validation"""
    youtube_domains = ['youtube.com', 'youtu.be', 'www.youtube.com', 'm.youtube.com']
    return any(domain in url.lower() for domain in youtube_domains)

def main():
    # Check if yt-dlp is installed
    try:
        import yt_dlp
    except ImportError:
        print("❌ yt-dlp is not installed.")
        print("Install it with: pip install yt-dlp")
        sys.exit(1)
    
    print("🎥 YouTube Video Downloader")
    print("=" * 30)
    
    # Get URL
    video_url = input("Please enter a YouTube URL: ").strip()
    
    if not validate_url(video_url):
        print("❌ Invalid YouTube URL. Please check and try again.")
        return
    
    # Choose interface
    use_gui = input("Use GUI for folder selection? (y/n): ").lower().strip() in ['y', 'yes']
    
    if use_gui:
        root = tk.Tk()
        root.withdraw()  # Hide main window
        save_dir = open_file_dialog()
        
        if save_dir:
            download_with_gui(video_url, save_dir)
        else:
            print("❌ No folder selected.")
        
        root.destroy()
    else:
        # Command line interface
        save_dir = input("Enter download folder path (or press Enter for current directory): ").strip()
        if not save_dir:
            save_dir = os.getcwd()
        
        if os.path.exists(save_dir):
            download_video(video_url, save_dir)
        else:
            print(f"❌ Directory '{save_dir}' does not exist.")

if __name__ == "__main__":
    main()