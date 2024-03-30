from pytube import YouTube
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox

"""YouTube Downloader for free
    : 1080p quality (enhanced birate)
    : 60 FPS (frametime)
    : mp4 File
    : No lag"""


# Made by Anshuman Tripathi

# YouTube Downloader:

def start():
    global userName

    filepath = str("C:/Users/" + userName + "/Downloads")
    root = Tk()
    root.title("YouTube Downloader")

    title = Label(root, text="YouTube Downloader", font=("Arial", '50', 'bold')).pack(pady=10, padx=20)

    credit = Label(root, text="Made by Anshuman Tripathi", font=("Arial", 18)).pack(pady=10)

    important = Label(root, text="Enter the URL of YouTube Video below the text box ", font=("Arial", 18, 'bold')).pack(pady=1)

    important2 = Label(root, text="and click on Download", font=("Arial", 18, 'bold')).pack(pady=10)

    link = StringVar()

    url = ttk.Entry(root, textvariable=link, font=("Arial", 18, 'bold'), justify="center", width=50)

    url.pack(pady=10)

    def downloadvideo():
        link = url.get()
        if link == "":
            messagebox.showinfo("YouTube Downloader", "Entry is blank, please put an URL inside the entry for continue")
        else:
            try:
                yt = YouTube(link)
                yt.streams.filter(progressive=1, file_extension="mp4")
                yt.streams.first().download(filepath)
                messagebox.showinfo("YouTube Downloader", "Downloaded Successfully")
            except:
                messagebox.showerror("YouTube Downloader", "Invalid URL, please try again")

    dwl = Button(root, text="Download video", font=("Arial", 18, 'bold'), width=20, command=downloadvideo)

    dwl.pack(pady=10)

    root.mainloop()

# Username Filer

user = Tk()
user.title("YouTube Downloader")
username = StringVar()
userName = ""
lbl1 = Label(user, text="Enter your windows username").pack(pady=10)
lbl2 = Label(user, text="If you other devices such as Mac, this downloader is not going to work.").pack(pady=10, padx=10)
user1 = ttk.Entry(user, textvariable=username, justify="center")
user1.pack(pady=10)
def makeroot():
    username = user1.get()
    global userName
    if username == "":
        messagebox.showinfo("YouTube Downloader", "The entry is not filled, please enter your username to continue")
    else:
        userName = username
        user.destroy()
        start()

butt1 = ttk.Button(user, text="Enter", command=makeroot).pack(pady=10)
lbl3 = Label(user, text="Why we are taking username?: ").pack()
lbl4 = Label(user, text="The downloaded youtube video will extracted into your Downloads ").pack()
lbl5 = Label(user, text="so your username will be taken as 'C:/Users/<your username>/Downloads'").pack(pady=10)

user.mainloop()