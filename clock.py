import tkinter as tk
import time

# create the root window
root = tk.Tk()
root.title("Simple Clock")  # set the window title

# create a label to display the time
time_label = tk.Label(root, font=("Helvetica", 32))
time_label.pack()

# update the time and display it on the label
def update_time():
    current_time = time.strftime("%I:%M:%S %p")  # get the current time
    time_label["text"] = current_time  # update the time on the label
    time_label.after(1000, update_time)  # call this function again after 1 second (1000 milliseconds)

# start the clock
update_time()
root.mainloop()  # start the main event loop

# made by KingTreemox aka Treemox