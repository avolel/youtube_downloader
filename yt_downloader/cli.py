import argparse
import logging
import sys
from pathlib import Path

from .downloader import download, DownloadError

def configure_logging(verbose: bool):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

def parse_args():
    parser = argparse.ArgumentParser(
        prog="ytsd",
        description="A simple production-ready YouTube downloader CLI tool.",
    )

    parser.add_argument(
        "-u",
        "--url",
        required=True,
        help="YouTube video URL",
    )

    parser.add_argument(
        "-o",
        "--output",
        default="downloads",
        help="Output directory (default: downloads)",
    )

    parser.add_argument(
        "-r",
        "--resolution",
        help="Video resolution (e.g., 720p, 1080p). Defaults to highest.",
    )

    parser.add_argument(
        "-a",
        "--audio-only",
        action="store_true",
        help="Download audio only (highest quality).",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose logging.",
    )

    return parser.parse_args()

def main():
    args = parse_args()
    configure_logging(args.verbose)

    output_dir = Path(args.output)

    try:
        download(
            url=args.url,
            output_dir=output_dir,
            resolution=args.resolution,
            audio_only=args.audio_only,
        )
        return 0

    except DownloadError as e:
        logging.error("Download failed: %s", e)
        return 1

    except KeyboardInterrupt:
        logging.warning("Download cancelled by user.")
        return 130


if __name__ == "__main__":
    sys.exit(main())