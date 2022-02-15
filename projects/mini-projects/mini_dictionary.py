from ast import Lambda
from statistics import mean
from tkinter import *
from tkinter import font
from urllib import response
from PIL import Image, ImageTk
import json
from difflib import get_close_matches

data_load = json.load("../Downloads/dictionary.json")

def search_word(word):
    if word in data_load:
        meaning_word.delete(1.0, END)
        meaning_word.config(fg="red")
        meaning_word.insert(END, data_load[word])
    
    elif len(get_close_matches(word, data_load.keys())):
        meaning_word.config(fg="red")
        meaning_word.delete(1.0, END)
        meaning_word.insert(END, "Were you finding {} and meaning is : {} ".format(get_close_matches(word, data_load.keys())[0],data_load[get_close_matches(word, data_load.keys())]))
        final = get_close_matches(word, data_load)

root = Tk()
root.title("MY OWN DICTIONARY")

image = Image.open('../Downloads/download.jpeg')
image_picture = ImageTk.PhotoImage(image)
dest_pic = Label(root, image=image_picture)
dest_pic.pack()

a = StringVar()
word_1 = Entry(root, textvariable=a, background="blue", fg="white", font=("arial", 40, "bold"))
word_1.place(relx=.185, rely=0.70, relwidth=.63, relheight=.082)

button_1 = Button(root, text="SEARCH THE WORD", command=lambda:search_word(a.get()), background="red", fg="white", font=("Arial", 40, "italic"))
button_1.place(relx=.25, rely=.85, relwidth=.50, relheight=.052)

meaning_word = Text(root, background="white", font=("Arial", 25, "bold"))
meaning_word.place(relx=.200, rely=.05, relwidth=.63, relheight=.16)


root.mainloop()