# Saatvik Kambhampati
# Feb 2021
import tkinter as tk;
from tkinter import *
import tkinter.filedialog;
from PIL import ImageTk,Image;
import glob;

class Main():
  def __init__(self):
    self.ImgFiles = [];
    self.window = tk.Tk();
    self.ImgPointer = 0;
  
  def showImg(self): 
    self.ThisImg = ImageTk.PhotoImage(Image.open(self.ListOfDirs[self.ImgPointer]));
    self.OpenImg = Label(image = self.ThisImg);
    self.OpenImg.pack();
  
  def goForward(self):
    if(self.ImgPointer == (len(self.ListOfDirs) - 1)):
      self.ImgPoint = 0;
      self.OpenImg.destroy();
    else:
      self.ImgPointer += 1;
      self.OpenImg.destroy();
    Exec = self.showImg();

  def goBackward(self):
    if(self.ImgPointer == 0):
      self.ImgPoint = len(self.ListOfDirs) - 1;
      self.OpenImg.destroy();
    else:
      self.ImgPointer -= 1;
      self.OpenImg.destroy();
    Exec = self.showImg();
    
  def buttons(self):
    self.ForwardButton = tk.Button(self.window, text = "-->", command = lambda: self.goForward());
    self.ForwardButton.pack(padx = 0, pady = 0, side = BOTTOM);
    self.BackwardButton = tk.Button(self.window, text = "<--", command = lambda: self.goBackward());
    self.BackwardButton.pack(padx = 0, pady = 0, side = BOTTOM);
  
  def getPath(self, DirPath):
    self.ListOfDirs = glob.glob(DirPath + "/*.png") + glob.glob(DirPath + "/*.jpg");
    if(len(self.ListOfDirs) != 0):
      Exec = self.showImg();
    else:
      self.ErrLabel = Label(self.window, text = "Please enter a directory with at least one .png or .jpg file.");
      self.ErrLabel.pack();
      self.Path.destroy();
      self.PathButton.destroy();
      self.pathEntryBox();
  
  def pathEntryBox(self):
    self.Path = tk.Entry(self.window, width = 100);
    self.Path.pack(padx = 0, pady = 0, side = TOP);
    self.dir = tk.filedialog.askdirectory();
    self.Path.insert(tk.END, self.dir);
    self.DirPath = self.Path.get();
    self.PathButton = tk.Button(self.window, text = "Enter", command = lambda: self.getPath(self.DirPath));
    self.PathButton.pack(padx = 0, pady = 0);

  def initializeWindow(self):
    self.window.title("Python Image Viewer")
    self.window.iconbitmap(); #Icon for window
  
  def mainLoop(self):
    self.window.mainloop();
  
main = Main();
main.initializeWindow();
main.buttons();
Path = main.pathEntryBox();
main.mainLoop();
