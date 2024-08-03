import re , io 
from mutagen.id3 import ID3


def is_youtube_link(url):
    youtube_regex = re.compile(
        r'^(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+$'
    )
    return bool(youtube_regex.match(url))


def extract_title(mp3_binary):
    tags = ID3(io.BytesIO(mp3_binary)).items()
    title_frame = next((frame for frame_id, frame in tags if frame_id == 'TIT2'), None)
    return title_frame.text[0].split("(")[0]



