# Musikun - youtube_dl based python mp3 processor
# Chelsea Chaffey 11/4/2022
# reference: https://www.codespeedy.com/download-youtube-video-as-mp3-using-python/ 

import youtube_dl
import sys
from metasong import Metasong
import requests
import os

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

def collect_url(url):
    try:
        download_mp3(url)
    except:
        print(f"ERROR: Is the url '{url}' valid?")

def command_collect(commands):
    '''
    download from youtube
    '''
    if (len(commands) < 2):
        print("Usage: collect <url>")
        return
    collect_url(command[1])

def command_collect_file(commands):
    '''
    download each track from file of urls
    '''
    if (len(commands) < 2):
        print("Usage: collectfile <filepath>")
        return
    try:
        with open(commands[1], 'r') as f:
            # peek each line in the file
            for url in f:
                if (url.strip()):
                    collect_url(url.strip())
    except OSError:
        print(f"Could not open or read file: {commands[1]}")
        return

def peek_url(url):
    '''
    check it is a youtube url
    print the metadata of one url
    '''
    if ( not url.startswith('https://www.youtube.com/watch?')):
        print(f"ERROR: URL '{url}' does not appear to be a youtube video.")
        return
    try:
        meta = Metasong(url)
        meta.printMetadata()
    except requests.exceptions.MissingSchema:
        print(f"ERROR: Invalid URL '{url}'.")

def command_peek(commands):
    '''
    print metadata that the url points to
    '''
    if (len(commands) < 2):
        print("Usage: peek <url>")
        return
    peek_url(commands[1])
    print('-' * os.get_terminal_size().columns)

def command_peek_file(commands):
    '''
    for each url in the file (separated by newlines), print metadata
    '''
    if (len(commands) < 2):
        print("Usage: peekfile <filepath>")
        return
    try:
        with open(commands[1], 'r') as f:
            # peek each line in the file
            for url in f:
                if (url.strip()):
                    peek_url(url.strip())
        print('-' * os.get_terminal_size().columns)
    except OSError:
        print(f"Could not open or read file: {commands[1]}")
        return

def command_view():
    '''
    List songs available in directory
    '''
    onlyfiles = [f for f in os.listdir('songs') if os.path.isfile(os.path.join('songs', f))]
    for file in onlyfiles:
        print(file)

def command_help():
    '''
    display help menu
    '''
    print("""Help menu:
    collect <url>           download music track from youtube url
    collectfile <filename>  download all music tracks in file
    play <song>             play given song
    peek <url>              check which music the url points to
    peekfile <filepath>     check details on text file containing list of urls
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
    elif (head == "collectfile"):
        command_collect_file(commands)
    elif (head == "peek"):
        command_peek(commands)
    elif (head == "peekfile"):
        command_peek_file(commands)
    elif (head == "view"):
        command_view()
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
