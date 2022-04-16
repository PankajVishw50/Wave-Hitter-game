import time
from tkinter import *
import pygame
from pygame import mixer
import random
from tkinter import messagebox
import webbrowser


# Functions
def glow(x):    # To make cubes Glow

    # Playing sound
    title.configure(fg=color[random.randint(0, 5)])
    mixer.music.load(f"Resources/0{random.randint(1, 3)}_beep.mp3")
    mixer.music.play()

    # Changing color
    x.configure(bg=color[random.randint(0, 5)])
    root.update()


def reverse(x):     # Reversing the Glow function
    x.configure(bg="#f5ede4")
    root.update()


def run_simulation(x): # Main Animation Running function

    glow(x)
    time.sleep(0.1)
    reverse(x)
    obj_index = objects.index(x)

    # Setting Horizontal Domain
    ratio = [0, 58]
    while True:
        if obj_index < ratio[1]:
            break
        else:
            ratio[0] += 58
            ratio[1] += 58

    # mapping
    run_map = [obj_index - 58, obj_index + 58,
               obj_index - 1, obj_index + 1,
               obj_index - 59, obj_index + 59,
               obj_index - 57, obj_index + 57]

    see = [0 for x in range(8)]  # condition for While loop

    # Main Loop
    while sum(see) != 8:

        if 0 < run_map[0] < len(objects):  # Top
            glow(objects[run_map[0]])
        else:
            see[0] = 1

        if len(objects) > run_map[1] > 0:  # Bottom
            glow(objects[run_map[1]])
        else:
            see[1] = 1

        if ratio[0] <= run_map[2] < ratio[1]:  # Left side
            glow(objects[run_map[2]])
        else:
            see[2] = 1

        if ratio[0] <= run_map[3] < ratio[1]:  # Right side
            glow(objects[run_map[3]])
        else:
            see[3] = 1

        if 0 < run_map[4] < len(objects):  # Right Upper Diagonal
            glow(objects[run_map[4]])
        else:
            see[4] = 1

        if run_map[5] < len(objects) and run_map[5] < len(objects):  # Right Lower Diagonal
            glow(objects[run_map[5]])
        else:
            see[5] = 1

        if run_map[6] > 0:  # Left Upper Diagonal
            glow(objects[run_map[6]])
        else:
            see[6] = 1

        if run_map[7] < len(objects):  # Left Lower Diagonal
            glow(objects[run_map[7]])
        else:
            see[7] = 1

        time.sleep(0.05)

        # <--------- Reversing Glow ------------->

        if run_map[0] > 0:  # Top
            reverse(objects[run_map[0]])
            run_map[0] -= 58

        if run_map[1] < len(objects):  # Bottom
            reverse(objects[run_map[1]])
            run_map[1] += 58

        if ratio[0] <= run_map[2] < ratio[1]:  # Left side
            reverse(objects[run_map[2]])
            run_map[2] -= 1

        if ratio[0] <= run_map[3] < ratio[1]:  # Right side
            reverse(objects[run_map[3]])
            run_map[3] += 1

        if run_map[4] > 0:  # Right Upper Diagonal
            reverse(objects[run_map[4]])
            run_map[4] -= 59

        if run_map[5] < len(objects):  # Right Lower Diagonal
            reverse(objects[run_map[5]])
            run_map[5] += 59

        if run_map[6] > 0:  # Left Upper Diagonal
            reverse(objects[run_map[6]])
            run_map[6] -= 57

        if run_map[7] < len(objects):  # Left Lower Diagonal
            reverse(objects[run_map[7]])
            run_map[7] += 57

    title.configure(fg="White")


def redirect(x):  # Redirecting to my Profile
    links = ["https://github.com/PankajVishw50", "https://www.linkedin.com/in/pankaj-vishw-4802a9232/"]
    webbrowser.open(links[x])

# <----------- Declaring Necessary Variables ----------->
objects = [str(x) for x in range(58 * 26)]  # Cube List
color = ["#eb389a", "#3111bf", "pink", "Orange", "#121a1f", "#3b0770"]
pygame.init()  # Initializing pygame for music player


# <------ Initializing root window -------->
root = Tk()
root.geometry("1280x720")
root.resizable(False, False)

root.title("Wave Hitter")
root.iconbitmap('Resources/Icons/wave_hitter.ico')  # Setting Window Icon

# <----------- Header --------------->
header = LabelFrame(root, width=1280, height=100, bg="#1c1a18")
header.grid_propagate(0)
header.pack()

github_label = Button(header, text="Github", font="Argentina 13",
                      fg="black", bg="White",
                      activebackground="Beige", activeforeground="Brown",
                      command=lambda: redirect(0))

linkedin_label = Button(header, text="Linkedin", font="Argentina 13",
                        fg="Black", bg="White",
                        activebackground="Beige", activeforeground="Brown",
                        command=lambda: redirect(1))

github_label.place(x=0, rely=0.7)
linkedin_label.place(x=60, rely=0.7)

title = Label(header, text="Wave hitter", font="Algerian 25", bg="#1c1a18", fg="White")  # Title (Wave Hitter)
title.place(relx=0.45, rely=0.3)

content = LabelFrame(root, bg="#50697d")
content.pack()


# <------ Creating Cubes -------->

def cube_creation():
    i = 0  # object indexing

    for x in range(26):
        for y in range(58):
            objects[i] = Label(content, height=1, width=2, bg="#f5ede4")
            objects[i].grid(row=x, column=y, pady=1, padx=1)
            i += 1

cube_creation()
messagebox.showinfo("Tips", "Click on cubes to See process running")


# <--------- Bounding cubes ------------>
def bind(x):
    x.bind("<Button-1>", lambda i: run_simulation(x))

for index, x in enumerate(objects):
    bind(x)


# Footer
root.mainloop()
