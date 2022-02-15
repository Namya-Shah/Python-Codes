from moviepy.editor import *

video = VideoFileClip("../Downloads/meme.mp4")
video.write_gif("final.gif")
