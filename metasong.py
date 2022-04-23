# simple python class to fetch data about the youtube video
# Chelsea Chaffey 11/04/2022

from bs4 import BeautifulSoup
import requests
import os
from eawtextwrap import EAWTextWrapper

class Metasong:
    '''
    Class that extracts some metadata from a youtube URL. 
    '''
    def __init__(self, url):
        self.url = url
        HEADER = {
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        response = requests.get(url, headers=HEADER)
        self.soup = BeautifulSoup(response.text, "html.parser")

    def getTitle(self):
        '''
        return title of video
        '''
        titleMetaSoup = self.soup.find("meta", property="og:title")
        return titleMetaSoup["content"] if titleMetaSoup else "unknown"

    def getDescription(self):
        '''
        return description
        '''
        titleMetaSoup = self.soup.find("meta", property="og:description")
        return titleMetaSoup["content"] if titleMetaSoup else "unknown"

    def getArtist(self):
        '''
        extract video author
        assumes that the video author is the artist of the music
        '''
        nameSoup = self.soup.find("link", itemprop="name")
        return nameSoup["content"] if nameSoup else "unknown"

    def getCanonURL(self):
        '''
        return canon url link
        '''
        urlSoup = self.soup.find("link", rel="canonical")
        return urlSoup["href"] if urlSoup else "unknown"
    
    def printMetadata(self):
        '''
        print nicely formatted details about the song
        '''
        width_char = os.get_terminal_size().columns
        wrapper = EAWTextWrapper(width=width_char, subsequent_indent = '               ')

        metadata = [
            f"       Title   {self.getTitle()}",
            f"     Channel   {self.getArtist()}",
            f" Description   {self.getDescription()}"
        ]
        for line in metadata:
            print('\n'.join(wrapper.wrap(line)))

