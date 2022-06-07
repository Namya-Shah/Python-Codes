from fileinput import filename
import os
import shutil
import time
import logging
from os.path import splitext

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Fill in below
source_dir = "/Users/neelshah/Downloads"
dest_dir_documents = "/Users/neelshah/Downloads/Documents"
dest_dir_music = "/Users/neelshah/Downloads/Music"
dest_dir_video = "/Users/neelshah/Downloads/Videos"
dest_dir_image = "/Users/neelshah/Downloads/Images"

image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]
video_extensions = [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".mpeg", ".mpg"]
audio_extensions = [".mp3", ".wav", ".wma", ".flac", ".aac", ".ogg"]
document_extensions = [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".csv", ".html", ".htm", ".xml", ".json"]

def make_unique(path):
    filename, extension = splitext(path)
    counter = 1