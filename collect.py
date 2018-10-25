import youtube_dl

PLAYLIST = "https://www.youtube.com/playlist?list=PLiZxWe0ejyv8CSMylrxb6Nx4Ii2RHbu_j"

opts = {
    "outtmpl": "data/%(id)s.%(ext)s",
    "subtitleslangs": ["en"],
    "writesubtitles": True,
    "subtitlesformat": "vtt",
    "format": "mp4/bestvideo[height>=720]",
    "keepvideo": True,
    "postprocessors": [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'nopostoverwrites': True,
        }
    ],
}

with youtube_dl.YoutubeDL(opts) as ydl:
    ydl.download([PLAYLIST])
