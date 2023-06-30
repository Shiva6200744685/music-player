from tkinter import filedialog
from tkinter import *
import pygame
import os

root = Tk()
root.title('Music Player')
# root.iconbitmap()
root.geometry("500x300")

pygame.mixer.init()

# adding menu bar
menubar = Menu(root)
root.config(menu=menubar)

# loading music
songs = []
current_song = " "
paused = False


def load_music():
    global current_song
    root.directory = filedialog.askdirectory()
    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if (ext == ".mp3"):
            songs.append((song))
#  uploading song on player
    for song in songs:
        songlist.insert("end", song)

    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]

# playing load_music


def play_music():
    global current_song, paused
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False


def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True


def next_music():
    global current_song, paused
    try:
        songlist.select_clear(0, END)
        songlist.select_set(songs.index(current_song)+1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
            pass

def prev_music():
    global current_song, paused
    try:
        songlist.select_clear(0, END)
        songlist.select_set(songs.index(current_song)+1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass




# creading organise
organizeMenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Organise", menu=organizeMenu)
organizeMenu.add_command(label="Add to Playlist", command=load_music)


songlist = Listbox(root, bg="black", fg="white", width=100, height=15)
songlist.pack()
# songlist.insert(END,"No Song Selected!")
play_buttn_img = PhotoImage(file='Projects/Code clause/play.png')
pause_buttn_img = PhotoImage(file='Projects/Code clause/pause.png ')
next_buttn_img = PhotoImage(file='Projects/Code clause/next.png ')
prev_buttn_img = PhotoImage(file='Projects/Code clause/previous.png ')

control_frame = Frame(root)
control_frame.pack()

play_buttn = Button(control_frame, image=play_buttn_img, borderwidth=0, command=play_music)
pause_buttn = Button(control_frame, image=pause_buttn_img, borderwidth=0, command=pause_music)
next_buttn = Button(control_frame, image=next_buttn_img, borderwidth=0, command=next_music)
prev_buttn = Button(control_frame, image=prev_buttn_img, borderwidth=0, command=prev_music)

play_buttn.grid(row=0, column=1, padx=7, pady=10)
pause_buttn.grid(row=0, column=2, padx=7, pady=10)
next_buttn.grid(row=0, column=3, padx=7, pady=10)
prev_buttn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop()


