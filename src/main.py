import tkinter as tk;
from tkinter import *
from PIL import ImageTk,Image;

class Main():
  def __init__(self):
    pass
  
  def initializeWindow(self):
    self.window = Tk();
    self.window.title("Python Image Viewer")
    self.window.iconbitmap(); #Icon for window
    self.MyImg = ImageTk.PhotoImage(Image.open());
    self.OpenImg = Label(image = self.MyImg);
    self.OpenImg.pack();
    self.window.mainloop();
    


main = Main();
main.initializeWindow();

