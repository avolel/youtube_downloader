import logging
from pathlib import Path
from typing import Optional 

from pytubefix import YouTube
from pytubefix.cli import on_progress

# Set up logging
logger = logging.getLogger(__name__)

class DownloadError(Exception):
    """Custom exception for download failures."""

def get_video_stream(yt: YouTube, resolution: Optional[str], file_format: str):
    streams = yt.streams.filter(progressive=True, file_extension=file_format)

    if resolution:
        stream = streams.filter(res=resolution).first()
        if not stream:
            raise DownloadError(f"{file_format} stream with resolution '{resolution}' not available.")
        return stream

    stream = streams.order_by("resolution").desc().first()
    if not stream:
        raise DownloadError(f"No progressive {file_format} streams available.")

    return stream


def get_audio_stream(yt: YouTube, file_format: str):
    stream = (
        yt.streams
        .filter(only_audio=True, file_extension=file_format)
        .order_by("abr")
        .desc()
        .first()
    )

    if not stream:
        raise DownloadError(f"No {file_format} audio streams available.")

    return stream


def download(
    url: str,
    output_dir: Path,
    resolution: Optional[str] = None,
    audio_only: bool = False,
    file_format: str = "mp4",
) -> Path:
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        logger.info("Fetching video information...")

        if audio_only:
            stream = get_audio_stream(yt, file_format)
        else:
            stream = get_video_stream(yt, resolution, file_format)

        output_dir.mkdir(parents=True, exist_ok=True)

        logger.info("Downloading: %s", yt.title)
        file_path = Path(stream.download(output_path=str(output_dir)))

        logger.info("Download complete: %s", file_path)
        return file_path

    except Exception as e:
        raise DownloadError(str(e)) from e