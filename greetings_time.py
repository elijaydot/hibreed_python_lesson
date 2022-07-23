
# Functions - a block of code that is independent and discreet, that performa a specific task.
# it helps to make code reusable and also make it clean and readable.

# modify the greet function to greet according to time
# first from the system and then from user.
import datetime
import time

currentTime = datetime.datetime.now()
currentTime.hour

# used to get and convert the current time into 24-hour mode and 12-hour mode
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t) # for 24-hour mode
current_time_now = time.strftime("%I:%M %p", t) # for 12-hour mode

def greetings():
    '''A function to get the appropriate greeting depending on which time of the day'''
    if currentTime.hour < 12:
        return 'Good morning,'
    elif 12 <= currentTime.hour < 18:
        return 'Good afternoon,'
    else:
        return 'Good evening,'

def greet():
    '''A function to greet a named user'''
    name = input('Enter your name: ')
    print(greetings(), name,'How are you?')
    
# Print out the current time and greet
print("The time is", current_time_now, 'OR', current_time)
greet()


'''
1//2 * 3

2/4
4/0.5

11 % 4

3 % 4

4 % 3

x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)
'''