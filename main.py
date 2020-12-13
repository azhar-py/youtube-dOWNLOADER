from pytube import YouTube
from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry('500x300')
root.title("Youtube Downloader ")
root.configure(background="#bab7fb")
root.resizable(0,0)
Title=Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold',bg="#bab7fb")
Title.pack()
link = StringVar()
linkin = Label(root, text = 'Paste  Vedio Link Here:', font = 'arial 15 bold',bg="#bab7fb")
linkin.place(x= 160 , y = 60)

link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
def Downloader():
    if link.get()=="":
        tkinter.messagebox.showerror("Error","Enter the URL ",parent=root)
    else:
        url =YouTube(str(link.get()))
        video = url.streams.first()
        video.download()

dbt=Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' , padx = 2, command = Downloader)
dbt.place(x=180 ,y = 150)

root.mainloop()

