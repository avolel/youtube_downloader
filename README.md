# Youtube-Downloader

YouTube downloader CLI tool built with pytubefix.

## Installation

pip install yt-downloader-andy

## Usage

Download highest resolution video:

ytsd -u URL

Download specific resolution:

ytsd -u URL -r 720p

Download audio only:

ytsd -u URL -a

Download audio in specific format:

ytsd -u URL -a -f webm

Download specific resolution and format:

ytsd -u URL -r 720p -f webm

Enable verbose logging:

ytsd -u URL -v
