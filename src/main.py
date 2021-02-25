import tkinter as tk;
from tkinter import *
from PIL import ImageTk,Image;
import glob;

class Main():
  def __init__(self):
    self.window = tk.Tk();
  

  def goForward(self):
    return;
  
  def goBack(self):
    return;
  
  def buttons(self):
    self.ForwardButton = tk.Button(self.window, text = "-->", command = goForward());
    #self.ForwardButton.place(x = 200, y = 100);
    self.ForwardButton.pack(padx = 0, pady = 0, side = BOTTOM);

    self.BackwardButton = tk.Button(self.window, text = "<--", command = goBack());
    #self.BackwardBUtton.place(x = 200, y = 100);
    self.BackwardButton.pack(padx = 0, pady = 0, side = BOTTOM);


  def getPath(self):
    print(glob.glob("/home/adam/*.txt"));

  def pathEntryBox(self):
    self.images = [];
    self.Path = tk.Entry(self.window, width = 100);
    #self.Path.place(x = 0, y = 0);
    self.Path.pack(padx = 0, pady = 0);

  def initializeWindow(self):
    self.window.title("Python Image Viewer")
    self.window.iconbitmap(); #Icon for window
    self.MyImg = ImageTk.PhotoImage(Image.open(r"C:\Users\sat.rk\Documents\Desktop\AintReadingAllThat.png"));
    self.OpenImg = Label(image = self.MyImg);
    self.OpenImg.pack();
  
  def mainLoop(self):
    self.window.mainloop();
  
  

main = Main();
main.chooseImageDir();
main.initializeWindow();
main.buttons();
main.mainLoop();

