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

# Input frame - content
user_input = Entry(input_frame, width=30, borderwidth=3, font=main_font)
user_input.grid(row=0, column=0)
add_button = Button(input_frame, text="Add", borderwidth=2,
                    font=main_font, bg=button_color)
add_button.grid(row=0, column=1)

# Text frame - content
list_box = Listbox(text_frame, height=15, width=45,
                   borderwidth=3, font=main_font)
list_box.grid(row=0, column=0)

# Button frame - content
remove_button = Button(button_frame, text="Remove item",
                       borderwidth=2, font=main_font)
clear_button = Button(button_frame, text="Remove list",
                      borderwidth=2, font=main_font)
save_button = Button(button_frame, text="Save",
                     borderwidth=2, font=main_font)
quit_button = Button(button_frame, text="Quit",
                     borderwidth=2, font=main_font, command=window.destroy)
remove_button.grid(row=0, column=0)
clear_button.grid(row=0, column=1)
save_button.grid(row=0, column=2)
quit_button.grid(row=0, column=3)

# Main loop
window.mainloop()
