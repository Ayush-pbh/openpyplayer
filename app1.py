from tkinter import *
import tkinter.messagebox as tkmsg
import pygame
from PIL import ImageTk
from PIL import Image
from mutagen.id3 import ID3
import os
import io
class App():
    def __init__(self):
        self.root = Tk()
        self.root.overrideredirect(1)
        self.root.maxsize(300,300)
        # self.frame = Frame(self.root, width=290, height=300,borderwidth=0,relief=RAISED)		
        # self.frame.pack_propagate(False)
        # self.frame.pack()
        self.bQuit = Button(self.root, text='q', command=self.root.quit)
        self.bQuit.pack()
        self.song = '/media/ayush/B050DFA050DF6B9A/Projects/Python Projects/MusicPlayer/Chidiya.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(self.song)
        self.playing = False
        self.initPlay = False
        self.img = ImageTk.PhotoImage(Image.open(self.getImage(self.song)).resize((300, 300))) # the one-liner I used in my app
        self.panel = Label(self.root, image=self.img)
        self.panel.pack(side='bottom', fill='both',expand='no',)
        self.panel.bind('<Button-1>',self.randyorten )
        self.panel.bind('<ButtonRelease-1>',self.stop_move)
        self.panel.bind('<B1-Motion>',self.do_move)
        #functions
    def getImage(self,source):
        img = ID3(self.song)
        datab = ''
        try:
            datab = img['APIC:'].data
        except:
            try:
                datab = img['APIC:3.jpeg'].data
            except:
                try:
                    datab = img['APIC:FRONT_COVER'].data
                except:
                    try:
                        datab = img['APIC:"Album cover"'].data
                    except:
                    	try:
                    		datab = img['APIC:3.png'].data
                    	except:
                        	return 'test.jpg'
        return io.BytesIO(datab)
    def toggleplaypause(self,event):
        # global self.playing
        # global self.initPlay
        if self.playing:
            #then pause
            pygame.mixer.music.pause()
            self.playing = False
        else:
            #then play
            if not self.initPlay:
                pygame.mixer.music.play()
                self.initPlay = True
                self.playing = True
                return    
            pygame.mixer.music.unpause()
            self.playing = True

#gui
# root = Tk()
# root.minsize(300,300)
# img = Image.open('./test.jpg')
# img = ImageTk.PhotoImage(img)

    def start_move(self,event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f'+{x}+{y}')

    def randyorten(self,event):
        self.toggleplaypause(event)
        self.start_move(event)

    def hello(self):
        tkmsg.showinfo('Popup','Hello There!')

app = App()
app.root.mainloop()
