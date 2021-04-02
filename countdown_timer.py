import time

def start_countdown(user_input_minutes):
    seconds = user_input_minutes * 60
    while seconds != 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    else:
        return True
