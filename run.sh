#!/bin/bash

python downloader.py
ffmpeg -ss 30 -i youtubeVideo.mp4 -t 30 -c copy croppedYoutubeVideo.mp4

