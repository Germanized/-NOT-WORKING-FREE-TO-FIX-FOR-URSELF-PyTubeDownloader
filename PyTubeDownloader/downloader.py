# PyTubeDownloader/downloader.py

import requests
import os

def download_video(url, output_dir=None, convert_to_mp3=False):
    api_url = "https://youtube-media-downloader2.p.rapidapi.com/ajaxSearch"
    headers = {
        "X-RapidAPI-Key": "FuckYou",
        "X-RapidAPI-Host": "youtube-media-downloader2.p.rapidapi.com"
    }
    querystring = {"url": url}
    response = requests.get(api_url, headers=headers, params=querystring)
    if response.status_code == 200:
        video_info = response.json()
        # Download video
        video_url = video_info.get("url")
        video_response = requests.get(video_url)
        if video_response.status_code == 200:
            if output_dir:
                video_filename = os.path.join(output_dir, "video.mp4")
            else:
                video_filename = "video.mp4"
            with open(video_filename, "wb") as video_file:
                video_file.write(video_response.content)
            # Convert to MP3 if requested
            if convert_to_mp3:
                os.system(f"ffmpeg -i {video_filename} {os.path.splitext(video_filename)[0]}.mp3")
                os.remove(video_filename)  # Delete the MP4 file
                return f"{os.path.splitext(video_filename)[0]}.mp3"
            else:
                return video_filename
        else:
            # Handle video download error
            return None
    else:
        # Handle error response
        return None

def download_audio(url, output_dir=None):
    api_url = "https://youtube-media-downloader2.p.rapidapi.com/ajaxSearch"
    headers = {
        "X-RapidAPI-Key": "475fb69180msh6173118b0eb9463p19b89ejsnb4fcb3c0e6f2",
        "X-RapidAPI-Host": "youtube-media-downloader2.p.rapidapi.com"
    }
    querystring = {"url": url}
    response = requests.get(api_url, headers=headers, params=querystring)
    if response.status_code == 200:
        audio_info = response.json()
        audio_url = audio_info.get("audio_url")
        if audio_url is None:
            # Audio URL not found
            return None
        audio_response = requests.get(audio_url)
        if audio_response.status_code == 200:
            if output_dir:
                audio_filename = os.path.join(output_dir, "audio.mp3")
            else:
                audio_filename = "audio.mp3"
            with open(audio_filename, "wb") as audio_file:
                audio_file.write(audio_response.content)
            return audio_filename
        else:
            # Handle audio download error
            return None
    else:
        # Handle error response
        return None
