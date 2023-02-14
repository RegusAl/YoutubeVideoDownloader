import tkinter
from pytube import YouTube
import customtkinter

def startDownloadHigh():
    try:
        youtubeLink = link.get()
        youtubeObject = YouTube(youtubeLink, on_progress_callback=onProgress)
        title.configure(text=youtubeObject.title, text_color="white")
        author.configure(text="Uploaded by " + youtubeObject.author, text_color="white")
        length.configure(text=str(youtubeObject.length) + " seconds", text_color="white")
        finishLabel.configure(text="")
        video = youtubeObject.streams.get_highest_resolution()
        video.download()
        finishLabel.configure(text="Downloaded", text_color="green")
    except:
        finishLabel.configure(text="Download Error!", text_color="red")

def startDownloadAudio():
    try:
        youtubeLink = link.get()
        youtubeObject = YouTube(youtubeLink, on_progress_callback=onProgress)
        title.configure(text=youtubeObject.title, text_color="white")
        author.configure(text="Uploaded by " + youtubeObject.author, text_color="white")
        length.configure(text=str(youtubeObject.length) + " seconds", text_color="white")
        finishLabel.configure(text="")
        audio = youtubeObject.streams.get_audio_only()
        audio.download()
        finishLabel.configure(text="Downloaded", text_color="green")
    except:
        finishLabel.configure(text="Download Error!", text_color="red")

def onProgress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per+"%")
    pPercentage.update()

    # Update progress bar
    progressBar.set(float(percentage_of_completion / 100))

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# UI elements
title = customtkinter.CTkLabel(app, text="Insert Youtube link")
title.pack(padx = 10, pady = 10)
author = customtkinter.CTkLabel(app, text="")
author.pack(padx = 10, pady = 10)
length = customtkinter.CTkLabel(app, text="")
length.pack(padx = 10, pady = 10)

# Link input
url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack()

# Download button

## Button for high resolution download
download_high_resolution = customtkinter.CTkButton(app, text="Download Highest Resolution", command=startDownloadHigh, height=40, width=150)
download_high_resolution.pack(padx=10, pady=15)

## Button for mp4 download
download_audio = customtkinter.CTkButton(app, text=" Download Audio Only (MP4) ", command=startDownloadAudio, height=40, width=150)
download_audio.pack(padx=10, pady=15)

# Footer
footer = customtkinter.CTkLabel(app, text="RegusAl ©2023")
footer.pack(pady=30)

# Run app
app.mainloop()