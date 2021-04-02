import time

def start_countdown(user_input_seconds):
    while user_input_seconds != 0: # while the variable is above 0 keep looping
        print(user_input_seconds)  # prints number of seconds left
        time.sleep(1)              # waits one secons using the time.sleep() function from the time module
        user_input_seconds -= 1    # subtracts 1 second from the variable to keep time
    '''
    Takes seconds as an input and counts down to 0 (Zero)
    When the function hits 0, returns None.
    '''
