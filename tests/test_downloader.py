# PyTubeDownloader/test_downloader.py

import unittest
import os
from .downloader import download_video, download_audio

class TestDownloader(unittest.TestCase):
    def test_download_video(self):
        # Test case 1: Downloading a video
        video_url = "https://www.youtube.com/watch?v=6_q_LHq85Cs"
        video_filename = download_video(video_url)
        self.assertIsNotNone(video_filename)
        self.assertTrue(os.path.exists(video_filename))
        os.remove(video_filename)

        # Test case 2: Downloading a non-existent video
        non_existent_video_url = "https://www.youtube.com/watch?v=nonexistent"
        non_existent_video_filename = download_video(non_existent_video_url)
        self.assertIsNone(non_existent_video_filename)

    def test_download_audio(self):
        # Test case 1: Downloading audio
        audio_url = "https://www.youtube.com/watch?v=6_q_LHq85Cs"
        audio_filename = download_audio(audio_url)
        self.assertIsNotNone(audio_filename)
        self.assertTrue(os.path.exists(audio_filename))
        os.remove(audio_filename)

        # Test case 2: Downloading audio from a non-existent video
        non_existent_audio_url = "https://www.youtube.com/watch?v=nonexistent"
        non_existent_audio_filename = download_audio(non_existent_audio_url)
        self.assertIsNone(non_existent_audio_filename)

if __name__ == '__main__':
    unittest.main()
