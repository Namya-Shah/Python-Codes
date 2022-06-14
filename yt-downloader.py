from tkinter import *
from pytube import YouTube
from moviepy.editor import *

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("BigSmoke's YouTube Downloader")
root.configure(bg="#f2eee3")

Label(root,
      text="Youtube Video Downloader",
      font="arial 20 bold",
      bg="#f2eee3",
      fg="red").pack()

link = StringVar()
Label(root,
      # PASTE THE YOUTUBE LINK HERE
      text="",
      font="arial 15 bold",
      bg="#f2eee3").place(x=40, y=40)

link_enter = Entry(root,
                   width=50,
                   textvariable=link).place(x=32, y=90)

def downloader():
    url = YouTube(str(link.get()))
    video = url.streams[1]
    video.download()
    Label(root,
          text="DOWNLOADED",
          font="arial 15",
          bg="#f2eee3",
          fg="red").place(x=185, y=185)
    return video.download()

def converter():
    mp3_file = f"/Users/neelshah/Downloads/YT-Downloaded/Converted Song.mp3"
    mp4_file = downloader()
    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()
    Label(root,
          text="CONVERTED",
          font="arial 15",
          bg="#f2eee3",
          fg="red").place(x=180, y=150)
    
download_mp4 = Button(root,
                      text="DOWNLOAD",
                      font="arial 15 bold",
                      bg="pale violet red",
                      padx=2,
                      command=downloader,
                      fg="blue").place(x=180, y=150)

convert_mp4 = Button(root,
                     text="Convert to mp3",
                     font="arial 15 bold",
                     bg="pale violet red",
                     padx=2,
                     command=converter,
                     fg="blue").place(x=180, y=210)

root.mainloop()