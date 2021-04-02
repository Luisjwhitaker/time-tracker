'''
    All functions take in time strings in the format HH:MM:SS
    Return converted time in integer format
    Example: convert_to_hours(01:60:00)
    Output: 2
'''

def convert_to_hours(input_string):
    hours,minutes,seconds = input_string.split(':')
    hours_total = int(hours) + (int(minutes)/60) + (int(seconds)/3600)
    return hours_total

def convert_to_minutes(input_string):
    hours,minutes,seconds = input_string.split(':')
    minutes_total = int(minutes) + (int(hours) * 60) + (int(seconds)/60)
    return minutes_total

def convert_to_seconds(input_string):
    hours,minutes,seconds = input_string.split(':')
    seconds_total = int(seconds) + (int(minutes)*60) + (int(hours)*3600)
    return seconds_total
