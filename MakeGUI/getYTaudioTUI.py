from rich import print
from pytube import YouTube
import datetime


def getAudioInfos():
    print("\n[b magenta]"+yt.title+"[/b magenta]")
    print("Duration: "+str(datetime.timedelta(seconds=yt.length)))
    print("Searching formats...")
    for stream in yt.streams.filter(only_audio=True):
        print(stream)

def downloadAudio(id):
    stream= yt.streams.get_by_itag(id)
    print("Downloading...")
    stream.download()

if __name__ == "__main__":
    url=input("What Youtube url to look at? ")
    yt = YouTube(url)
    getAudioInfos()
    id=int(input("What itag to download? "))
    downloadAudio(id)