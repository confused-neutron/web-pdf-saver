#matplt, fpdf and numpy, pyauto
import time
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
import pyautogui
import tkinter as tk


def get_page():
	x1 = frame.winfo_rootx()
	x2 = frame.winfo_rootx() + frame.winfo_width()
	y1 = frame.winfo_rooty()
	y2 = frame.winfo_rootx() + frame.winfo_height()

	return np.array(pyautogui.screenshot(region=(frame.winfo_rootx(), frame.winfo_rooty(), frame.winfo_width(), frame.winfo_height())))

def flip_page():
	pyautogui.click(765, 790)

def main():
	save_Loc = inputtxt2.get("1.0", "end-1c") 
	doc = inputtxt.get("1.0", "end-1c")
	num_pages = inputtxt3.get("1.0", "end-1c")
	time.sleep(2)
	pdf = None

	for pg_num in range(int(num_pages)):
		print('On page', str(pg_num + 1))
		page = get_page()
		plt.imsave(save_Loc + doc + str(pg_num) + '.png', page)
		time.sleep(0.1)
		print(save_Loc)

def Start():

	wx, wy = frame.winfo_rootx(), frame.winfo_rooty()
	print(wx, wy)
	if __name__ == '__main__':
	  main()


# Top level window 
frame = tk.Tk() 
frame.title("Screenshot PDF maker") 
frame.geometry('400x200') 

# TextBox Creation 
inputtxt = tk.Text(frame, 
				height = 2, 
				width = 20) 

inputtxt2 = tk.Text(frame, 
				height = 2, 
				width = 20) 

inputtxt3 = tk.Text(frame, 
				height = 2, 
				width = 20) 



# Button Creation 
startButton = tk.Button(frame, 
						text = "Start", 
						command = Start)


# Create label 
bookName = tk.Label(frame, text = "Book name") 
bookName.config(font =("Arial", 8)) 

# Create label 
ins = tk.Label(frame, text = "Arrange and shape the window so that it covers the entire page.") 
ins.config(font =("Arial", 9)) 


# Create label 
location = tk.Label(frame, text = "Location") 
location.config(font =("Arial", 7)) 

# Create label 
pageNum = tk.Label(frame, text = "Number of pages") 
pageNum.config(font =("Arial", 7)) 

ins.pack()
bookName.pack()
inputtxt.pack()
location.pack()
inputtxt2.pack() 
inputtxt2.insert(tk.END, "D:\Books")
pageNum.pack() 
inputtxt3.pack()
startButton.pack() 

tk.mainloop()