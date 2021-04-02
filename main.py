from tkinter import *
import countdown_timer
import log_data
import time_converter
'''
def add_10_minutes(): # for future funtionality allowing for an "add 10 minutes" button | may ass functionality for 5 minute and 1 hr timer too.
    pass
def clear_entry():# for future funtionality allowing for a "reset" button
    pass
'''
# colates data and sends it to be saved in a database of some sort
def save_to_database():
    global time_elapsed
    global task_selected
    log_data.log_sqlite(time_elapsed,task_selected)

# funcion that captures selected value from popup
def on_select(selected):
    global task_selected
    task_selected = selected

# define what happens when you press the button
def on_click():
    global time_remaining
    global time_elapsed
    time_elapsed = user_entry.get()
    seconds = time_converter.convert_to_seconds(user_entry.get()) # feeds the input into the convert_to_seconds function
    countdown = countdown_timer.start_countdown(seconds)    # feeds the seconds into the start_countdown function| when done returns None type
    time_remaining = countdown
    if countdown == None: # waits for start_countdown to return None, signifying the countdown is over.
        popup_window()

def popup_window():
    global task_selected
    popup = Toplevel()
    popup.title('Timer Done')
    popup.geometry('400x400')

    questionare_label = Label(popup, text='What where you working on?')
    task_dropdown = OptionMenu(popup, clicked, *tasks, command=on_select)
    submit_button = Button(popup, text='Track Data', command=save_to_database)

    questionare_label.grid(row=0, column=0)
    task_dropdown.grid(row=1, column=0)
    submit_button.grid(row=2, column=0)

    popup.mainloop()


# initialize tkinter window, size it, and give it a name.
root = Tk()
root.title('Time Tracker')
root.geometry('400x400')

# string var to display time remaining
time_remaining = StringVar()
# string var for dropdown (OptionMenu) default option
clicked = StringVar()
clicked.set('Select Task Type')
# options for dropdown menue
tasks = [
    'Python',
    'Pland off',
    'Unpland off',
    'Frontend Dev',
    'Unpland "work"',
]

# set widgets
input_request_label = Label(root,text='Enter in HH:MM:SS format')
user_entry = Entry(root)
start_btn = Button(root, text='Start Timer', command=on_click)
time_left_label = Label(root,text=time_remaining)

# place widgets for display
input_request_label.pack()
user_entry.pack()
start_btn.pack()
time_left_label.pack()

# run mainloop
root.mainloop()
