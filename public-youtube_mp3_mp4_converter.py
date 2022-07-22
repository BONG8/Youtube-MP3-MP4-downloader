from pytube import YouTube 
import os
import os.path
import moviepy
import moviepy.editor

#get the video url
video_url = str(input("Insert the link here:"))
#for getting the left rotated slang
slang = r"\a"
slang = slang[0]


#download the video in mp4 format
def Downloadmp4(video):
    videoname = str(input("Insert the name of the video without extension: "))
    
    video.download(output_path = path_, filename = videoname + ".mp4")
    
    if (option_ == 1 or option_ == 3):
        OptionOneThree(videoname)
    else:
        print("MP4 file downloaded succesfully")
        
        
# write an mp3 file and if option_ variable is 1, delete mp4 file
def OptionOneThree(videoname):
    if (os.path.exists(path_)):
            Videoclip = moviepy.editor.VideoFileClip(path_ + slang + videoname + ".mp4")
           
    audioclip = Videoclip.audio
    
    
    audioclip.write_audiofile(path_ + slang + videoname + ".mp3")
    audioclip.close()   
    Videoclip.close() 
    if (option_ == 1):  
        os.remove(path_ + slang + videoname + ".mp4")
   
    print("downloaded succesfully")
    

#choose the path where to save the file
path_ = str(input("Insert the path where to save the file or the files: ")) 

print("The video url is: " + video_url)

#create an Youtube object with the video url
yt = YouTube(video_url)
print(yt.title)
print(str(yt.views) + " views" )
print(" 1. Download MP3 file \n 2. Download MP4 file \n 3. Download MP3 file + MP4 file")
option_ = int(input())

#get the video in highest resolution
yt = yt.streams.get_highest_resolution()

Downloadmp4(yt)


    
    







