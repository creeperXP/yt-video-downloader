# important for downloading videos (need access to YoutubeDL functions)
import yt_dlp

ydl_aspects = {
    'format': 'bestvideo+bestaudio/best',  # best overall quality
    'merge_output_format': 'mp4',  # if audio/video are separated, merge into 1 video
    'noplaylist': True,  # don't download the entire playlist even if link has "playlist" in it
} 

# download function takes youtube url and
def download(url):
    with yt_dlp.YoutubeDL(ydl_aspects) as ydl: # resource cleaned up/ydl object creation from YoutubeDL class
        ydl.download([url]) # downloads video by calling YoutubeDL class function

# continue downloading user's videos until they say 0 
tracker = 1
while tracker == 1:
    link = input("Enter youtube URL to download: ") # get user youtube link from input
    noSpaceLink = link.strip() # remove trailing/leading spaces

    download(noSpaceLink)
    tracker = int(input("Enter '1' if you want to download more videos\nEnter '0' if you don't: "))
