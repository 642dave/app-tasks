from tkinter import *

# Window
window = Tk()
window.title("list tasks")
window.minsize(400, 400)
window.iconbitmap("icon.ico")
window.resizable(False, False)

# Main fonts, colors
main_font = ("Times New Roman", 12)
main_color = "#090909"
button_color = "#4d4d4d"
fonts_color = "white"
window.config(bg=main_color)


# Functions
def add_text():
    list_box.insert(END, user_input.get())
    user_input.delete(0, END)


def remove_text_item():
    list_box.delete(ANCHOR)


def clear_all_list():
    list_box.delete(0, END)


def save_tasks():
    with open("tasks_save.txt", "w") as file:
        my_tasks = list_box.get(0, END)
        for one_task in my_tasks:
            if one_task.endswith("\n"):
                file.write(f"{one_task}")
            else:
                file.write(f"{one_task}\n")


def open_tasks():
    try:
        with open("tasks_save.txt", "r") as file:
            for one_line in file:
                list_box.insert(END, one_line)
    except:
        print("Error, failed to open file! ")


# Frames
input_frame = Frame(window, bg=main_color)
text_frame = Frame(window, bg=main_color)
button_frame = Frame(window, bg=main_color)
input_frame.pack()
text_frame.pack()
button_frame.pack()

# Input frame - content
user_input = Entry(input_frame, width=30, borderwidth=3, font=main_font)
user_input.grid(row=0, column=0, padx=5, pady=5)
add_button = Button(input_frame, text="Add", borderwidth=4,
                    font=main_font, fg=fonts_color, bg=button_color, command=add_text)
add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=24)

# Scrollbar
text_scrollbar = Scrollbar(text_frame)
text_scrollbar.grid(row=0, column=1, sticky=N+S)

# Text frame - content
list_box = Listbox(text_frame, height=15, width=40,
                   borderwidth=3, font=main_font, yscrollcommand=text_scrollbar.set)
list_box.grid(row=0, column=0)

# Listbox and Scrollbar connection
text_scrollbar.config(command=list_box.yview)

# Button frame - content
remove_button = Button(button_frame, text="Remove item",
                       borderwidth=4, font=main_font, fg=fonts_color, command=remove_text_item, bg=button_color)
clear_button = Button(button_frame, text="Remove list",
                      borderwidth=4, font=main_font, fg=fonts_color, command=clear_all_list, bg=button_color)
save_button = Button(button_frame, text="Save",
                     borderwidth=4, font=main_font, fg=fonts_color, command=save_tasks, bg=button_color)
quit_button = Button(button_frame, text="Quit",
                     borderwidth=4, font=main_font, fg=fonts_color, command=window.destroy, bg=button_color)
remove_button.grid(row=0, column=0, padx=5, pady=10, ipadx=10)
clear_button.grid(row=0, column=1, padx=5, pady=10, ipadx=10)
save_button.grid(row=0, column=2, padx=5, pady=10, ipadx=10)
quit_button.grid(row=0, column=3, padx=5, pady=10, ipadx=10)

open_tasks()

# Main loop
window.mainloop()