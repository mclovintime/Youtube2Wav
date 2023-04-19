import sys
import os
from pytube import YouTube
from moviepy.editor import AudioFileClip

# McLovin, Anno Domini 2023
# I love you
# Please enter python youtube2wav.py <youtube_url>

def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
    output_filename = f"{yt.title}.mp4"
    stream.download(filename=output_filename)
    return output_filename


def convert_to_wav(input_filename):
    audio = AudioFileClip(input_filename)
    output_filename = f"{input_filename.split('.')[0]}.wav"
    audio.write_audiofile(output_filename)
    return output_filename


def main():
    if len(sys.argv) != 2:
        print("Usage: python yt_to_wav.py <youtube_url>")
        return

    url = sys.argv[1]
    input_filename = download_video(url)
    output_filename = convert_to_wav(input_filename)

    # delete the intermediate MP4 file
    os.remove(input_filename)

    print(f"Downloaded and converted video to {output_filename}")


if __name__ == "__main__":
    main()