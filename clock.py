import tkinter as tk
import time

def time_function():
    current_time = time.strftime("%H:%M:%S")  # Get current time in HH:MM:SS format
    clock_label.config(text=current_time)  # Update the label with the current time
    clock_label.after(1000, time_function)  # Call the function every 1000ms (1 second)

# Set up the window
window = tk.Tk()
window.title("Digital Clock")

# Create a label to display the time
clock_label = tk.Label(window, font=("Helvetica", 48), background="black", foreground="white")
clock_label.pack()

# Call the time function to update the clock
time_function()

# Run the Tkinter event loop
window.mainloop()