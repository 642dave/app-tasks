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

# Main loop
window.mainloop()