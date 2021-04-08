# You need to import the pytube module to download videos and the os module from python to use the "folder organizing" functions
from pytube import Playlist, YouTube
import os


# Here we ask for a folder name and assign it to the variable "folder"
print("Input the folder name\n")

folder = str(input())

# The mkdir function from the os module allows us to create the folder and the chdir changes the current directory 
# to the folder we've just created
if not (os.path.isdir(folder)):

    os.mkdir(folder)

else:

    print("Ok, this folder exist...")


os.chdir(folder)

print("Press y for video or p for playlist download")

opt = str(input())

if opt == 'y':

    print("Input the video link\n")

    ytp = YouTube(str(input())).streams.first().download()
    
elif opt == 'p':
    
    print("Input the playlist link\n")

    ytp = Playlist(str(input()))

    print(f'Downloading a playlist: {ytp.title}')

    for video in ytp.videos:
        
        videoTitle = video.title
        
        print(f'- Title: {videoTitle}')

        if not (os.path.isfile(f'./{videoTitle}.mp4')):
            
            print('----- Downloading video...')
            
            video.streams.first().download()
        
        else:

            print('----- This video exist locally! Downloading the next video...')

        
else:
    
    print("Wrong!\n")


print("Finished!\n")
