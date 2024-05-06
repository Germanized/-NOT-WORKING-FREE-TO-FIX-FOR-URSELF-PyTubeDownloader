# test_script.py

from PyTubeDownloader import download_video, download_audio

def main():
    print("Welcome to PyTubeDownloader!")
    url = input("Enter the YouTube video URL: ")
    choice = input("Enter 'v' to download video or 'a' to download audio: ")

    if choice.lower() == 'v':
        # Download video
        video_filename = download_video(url)
        if video_filename:
            print("Downloaded video:", video_filename)
        else:
            print("Failed to download video.")
    elif choice.lower() == 'a':
        # Download audio
        audio_filename = download_audio(url)
        if audio_filename:
            print("Downloaded audio:", audio_filename)
        else:
            print("Failed to download audio.")
    else:
        print("Invalid choice. Please enter 'v' or 'a'.")

if __name__ == "__main__":
    main()
