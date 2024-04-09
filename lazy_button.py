from tkinter import * # import the tkinter module
from time import * # import the time module
import webbrowser # import the webbrowser module

# function to update the time and date
def update():
	time_string = strftime("%I:%M:%S %p") # %I: hour, %M: minute, %S: second, %p: AM/PM
	time_label.config(text=time_string)
	
	date_string = strftime("%d %B %Y (%A)") # %d: day, %B: month, %Y: year, %A: day of the week
	date_label.config(text=date_string)	

	time_label.after(1000, update) # update the time every 1000ms = 1s

# function to open the URL
def open_url():
	webbrowser.open("https://profile.intra.42.fr/")
def open_locatepeer():
	webbrowser.open("https://locatepeer.vercel.app/")
def open_slot():
	webbrowser.open("https://profile.intra.42.fr/slots")
def open_github():
	webbrowser.open("https://github.com/wenjuin95")

window = Tk() # create a window
window.geometry("500x175") # width x height
window.configure(bg="#3d3d3d") # background color

# time and date labels
time_label = Label(window, font=("Math Sans", 40), bg="#3d3d3d", fg="#d4d4d4") 
time_label.pack() 

# date label
date_label = Label(window, font=("Math Sans", 30), bg="#3d3d3d", fg="#d4d4d4")
date_label.pack()

# call the update function
update()

button_frame = Frame(window, bg="#3d3d3d")
button_frame.pack()

# button to open the URL
myButton = Button(button_frame, text="Open Intra", padx=10, pady=10, bg="light gray", command=open_url)
myButton.pack(side=LEFT, padx=10, pady=10)

# button to open the URL
locateButton = Button(button_frame, text="Open locate", padx=10, pady=10, bg="light gray", command=open_locatepeer)
locateButton.pack(side=LEFT, padx=10, pady=10)

# button to open the slots
slotButton = Button(button_frame, text="Open Slots", padx=10, pady=10, bg="light gray", command=open_slot)
slotButton.pack(side=LEFT, padx=10, pady=10)

# open github
githubButton = Button(button_frame, text="Open Github", padx=10, pady=10, bg="light gray", command=open_github)
githubButton.pack(side=LEFT, padx=10, pady=10)

window.mainloop() # run the window