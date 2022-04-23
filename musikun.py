# Musikun - youtube_dl based python mp3 processor
# Chelsea Chaffey 11/4/2022
# reference: https://www.codespeedy.com/download-youtube-video-as-mp3-using-python/ 

import youtube_dl
import sys
from metasong import Metasong
import requests

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

def command_collect(commands):
    '''
    download from youtube
    '''
    if (len(commands) < 2):
        print("Usage: collect <url>")
        return
    try:
        download_mp3(commands[1])
    except:
        print(f"command failed. \nIs the url '{commands[1]}' valid?")

def command_peek(commands):
    '''
    print metadata that the url points to
    '''
    if (len(commands) < 2):
        print("Usage: peek <url>")
        return
    try:
        meta = Metasong(commands[1])
        meta.printMetadata()
    except requests.exceptions.MissingSchema:
        print(f"Invalid URL '{commands[1]}'. Try a different URL.")

def command_help():
    '''
    display help menu
    '''
    print("""Help menu:
    collect <url>           download music track from youtube url
    play <song>             play given song
    peek <url>              check which music the url points to
    view                    see current downloaded music
    ---
    help                    display the help menu
    quit                    exit the program""")


def handle_command(command):
    '''
    interpret user commands and run appropriate logic
    return False if the program is to terminate
    '''
    commands = command.split()
    if (len(commands) == 0):
        return True
    head = commands[0].lower()
    if (head == "quit"):
        return False
    elif (head == "help"):
        command_help()
    elif (head == "collect"):
        command_collect(commands)
    elif (head == "peek"):
        command_peek(commands)
    elif (head == "view"):
        print("not implemented yet")
    elif (head == "play"):
        print("not implemented yet")
    else:
        print("Invalid command. Type \"help\" to access the help menu.")
    return True
    

if __name__ == "__main__":
    print("Welcome to ~Musikun~")
    loop = True
    while (loop):
        command = input("->> musikun~: ")
        loop = handle_command(command)
