from tkinter import *
from PIL import ImageTk,Image
import countdown_timer
import log_data
import time_converter

'''
def add_10_minutes(): # for future funtionality allowing for an "add 10 minutes" button | may add functionality for 5 minute and 1 hr timer too.
    pass
def clear_entry(): # for future funtionality allowing for a "reset" button
    pass
'''

# -- variables --
background_color = '#74e57f'
font_color = '#fff'
default_font = ('Raleway', 20)
task_selected = 'None selected' # default value for OptionMenu
#logged_label_data = '' # placeholder for 'data saved' promt (Currently not working)

# colates data and sends it to be saved in a database of some sort
def save_to_database():
    global time_elapsed
    global task_selected
    #global logged_label_data
    #logged_label_data = 'Data Saved!'
    log_data.log_sqlite(time_elapsed,task_selected)

# funcion that captures selected value from popup
def on_select(selected):
    global task_selected
    task_selected = selected

# define what happens when you press the button
def on_click():
    #global time_remaining
    global time_elapsed
    time_elapsed = f'{hour_entry.get()}:{minute_entry.get()}:{second_entry.get()}'
    seconds = time_converter.convert_to_seconds(f'{hour_entry.get()}:{minute_entry.get()}:{second_entry.get()}') # feeds the input into the convert_to_seconds function
    countdown = countdown_timer.start_countdown(seconds)    # feeds the seconds into the start_countdown function| when done returns None type
    #time_remaining = countdown
    if countdown == None: # waits for start_countdown to return None, signifying the countdown is over.
        popup_window()

def popup_window():
    global task_selected
    #global logged_label_data
    popup = Toplevel()
    popup.title('Times Up!')
    popup.geometry('500x300')
    popup.configure(bg=background_color)

    questionare_label = Label(popup, text='What where you working on?', font=default_font, bg=background_color, fg=font_color)
    task_dropdown = OptionMenu(popup, clicked, *tasks, command=on_select)
    task_dropdown.config(font=default_font, bg=background_color, fg=font_color)
    submit_button = Button(popup, text='Track Data', command=save_to_database, font=default_font, bg=background_color, fg=font_color)
    #logged_label = Label(popup, text=logged_label_data, font=default_font, bg=background_color, fg=font_color)

    questionare_label.place(relx=0.5, rely=0.2, anchor=CENTER)
    task_dropdown.place(relx=0.5, rely=0.4, anchor=CENTER)
    submit_button.place(relx=0.5, rely=0.6, anchor=CENTER)
    #logged_label.place(relx=0.5, rely=0.8, anchor=CENTER)

    popup.mainloop()


# initialize tkinter window, size it, and give it a name.
root = Tk()
root.title('Trakkey Time')
root.geometry('500x600')
root.configure(bg=background_color)

# string var to display time remaining
time_remaining = StringVar()

# string var for dropdown (OptionMenu) default option
clicked = StringVar()
clicked.set('Select Task Type')

# options for dropdown menue
tasks = [
    'Python coding',
    'Pland free time',
    'Unpland free time',
    'Frontend Development coding',
    'Procrastination "work"',
    'Other'
]

# set widgets
canvas = Canvas(root, width=500, height=250)
input_request_label = Label(root,text='Enter in HH:MM:SS format', font=default_font, bg=background_color, fg=font_color)
colon_label_1 = Label(root,text=':', font=default_font, bg=background_color, fg=font_color)
colon_label_2 = Label(root,text=':', font=default_font, bg=background_color, fg=font_color)
hour_entry = Entry(root, width=8, font=default_font)
minute_entry = Entry(root, width=8, font=default_font)
second_entry = Entry(root, width=8, font=default_font)
start_btn = Button(root, text='Start Timer', command=on_click, font=default_font, bg=background_color, fg=font_color)

# add default values to entry boxes
hour_entry.insert(END, '00')
minute_entry.insert(END, '00')
second_entry.insert(END, '00')

# place widgets for display
canvas.grid(columnspan=5)
logo = ImageTk.PhotoImage(Image.open('logo.png'))
logo_label = Label(image=logo)
logo_label.image=logo
logo_label.grid(row=0,column=0,columnspan=5)
input_request_label.grid(row=1,column=0,columnspan=5)
hour_entry.grid(row=2,column=0)
colon_label_1.grid(row=2,column=1)
minute_entry.grid(row=2,column=2)
colon_label_2.grid(row=2,column=3)
second_entry.grid(row=2,column=4)
start_btn.grid(row=3,column=0,columnspan=5, pady=20)


# run mainloop
root.mainloop()
