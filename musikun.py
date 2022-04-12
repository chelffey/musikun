# Musikun - youtube_dl based python mp3 processor
# Chelsea Chaffey 11/4/2022
# reference: https://www.codespeedy.com/download-youtube-video-as-mp3-using-python/ 

import youtube_dl
import sys

def download_mp3(url):
    '''
    save mp3 file
    '''
    video_info = youtube_dl.YoutubeDL().extract_info(url = url,download=False)
    filename = f".\songs\{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
        '--embed-thumbnail':True,
        '--add-metadata':True,
        '--write-description':True,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print(f"Download complete... {filename}")

def parse_args(argv):
    '''
    return the url if there is one
    '''
    if (len(argv) < 2):
        print(f"Usage: {argv[0]} <url>")
        exit(1)
    return argv[1]

if __name__ == "__main__":
    url = parse_args(sys.argv)
    download_mp3(url)
    exit(0)