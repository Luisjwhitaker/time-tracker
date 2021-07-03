import sqlite3
def log_sqlite(*data, database_name=None):
    print(f'Data Saved as {data}')

    # CREATE sqlite3 database:
    """conn = sqlite3.connect('time.db')
    c = conn.cursor()
    c.execute('''CREATE Table logs (
            time_elapsed text,
            task_selected text
            )''')
    conn.commit()
    conn.close()"""

    # INSERT INTO sqlite3 database:
    """conn = sqlite3.connect('stool_log.db')
    c = conn.cursor()
    c.execute("INSERT INTO logs VALUES(:time_elapsed,:task_selected)",{
            'time_elapsed': dt.strftime("%B %d,%Y"),
            'task_selected': dt.strftime("%H:%M %Z")
    })
    conn.commit()
    conn.close()
    messagebox.showinfo('showinfo','submitted')"""

'''
    This is meant to be an intermediery between the data I track and what database it is stored.
    right now it just prints out the data you put in it.
    return string type
'''
