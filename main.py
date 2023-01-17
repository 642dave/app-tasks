from tkinter import *

# Window
window = Tk()
window.title("list tasks")
window.minsize(400, 400)
window.iconbitmap("icon.ico")
window.resizable(False, False)

# Fonts, colors
main_font = ("Times New Roman", 12)
main_color = "#dd7f00"
button_color = "#e2cff4"
window.config(bg=main_color)

# Frames
input_frame = Frame(window, bg=main_color)
text_frame = Frame(window, bg=main_color)
button_frame = Frame(window, bg=main_color)
input_frame.pack()
text_frame.pack()
button_frame.pack()

# Main loop
window.mainloop()