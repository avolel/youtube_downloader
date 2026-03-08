# yt-downloader-andy

A simple, production-ready YouTube downloader CLI tool built with [`pytubefix`](https://github.com/JuanBindez/pytubefix).

## Installation

```bash
pip install yt-downloader-andy
```

## Usage

```bash
ytsd -u <YouTube URL> [options]
```

### Options

| Flag | Long form | Description | Default |
|------|-----------|-------------|---------|
| `-u` | `--url` | YouTube video URL *(required)* | — |
| `-o` | `--output` | Output directory | `downloads` |
| `-r` | `--resolution` | Video resolution (e.g. `720p`, `1080p`) | Highest available |
| `-a` | `--audio-only` | Download audio only (highest quality) | `false` |
| `-f` | `--format` | File format: `mp4` or `webm` | `mp4` |
| `-v` | `--verbose` | Enable verbose logging | `false` |

### Examples

**Download a video at the highest available resolution:**
```bash
ytsd -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

**Download at a specific resolution:**
```bash
ytsd -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -r 720p
```

**Download audio only:**
```bash
ytsd -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -a
```

**Download to a custom directory in webm format:**
```bash
ytsd -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -o ~/Videos -f webm
```

**Verbose output:**
```bash
ytsd -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -v
```

## Requirements

- Python >= 3.8
- [`pytubefix`](https://pypi.org/project/pytubefix/) >= 6.0.0

## Links

- [GitHub Repository](https://github.com/avolel/youtube-downloader)
- [PyPI Package](https://pypi.org/project/yt-downloader-andy/)