import tkinter as tk;
from tkinter import *
from PIL import ImageTk,Image;

class Main():
  def __init__(self):
    self.window = Tk();
  
  def buttons(self):
    self.ForwardCanvas = tk.Canvas(self.window, width = 20, height = 26, background = "blue");
    self.ForwardCanvas.pack();
    self.ForwardButton = tk.Button(self.window, text = "-->");
    self.ForwardButton.pack(padx = 75, pady = 0);
    #self.ForwardCanvas.create_window(20, 15, window = self.ForwardButton);



  def chooseImage(self):
    self.CanvasPath = tk.Canvas(self.window, width = 150, height = 30, background = "green");
    self.CanvasPath.pack();
    self.Path = tk.Entry(self.window) 
    self.CanvasPath.create_window(75, 20, window = self.Path)

  def initializeWindow(self):
    self.window.title("Python Image Viewer")
    self.window.iconbitmap(); #Icon for window
    self.MyImg = ImageTk.PhotoImage(Image.open(r"C:\Users\sat.rk\Documents\Desktop\AintReadingAllThat.png"));
    self.OpenImg = Label(image = self.MyImg);
    self.OpenImg.pack();
  
  def mainLoop(self):
    self.window.mainloop();
  
  

main = Main();
main.chooseImage();
main.initializeWindow();
main.buttons();
main.mainLoop();

