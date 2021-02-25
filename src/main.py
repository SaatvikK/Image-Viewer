import tkinter as tk;
from tkinter import *

class Main():
  def __init__(self):
    pass
  
  def initializeWindow(self):
    self.window = Tk();
    self.window.title("Python File Explorer")
    self.window.mainloop();



main = Main();
main.initializeWindow();

