
# list
from re import I


student_data = [1, 2.2, 'Python']

print("student data[0:3] =" , student_data[0:3])

# Tuple - ordered list. it cannot be changed. you cannot re-assigna value
# if you dont want your data to change store it in a tuple
# if you want your data to change, store in a list
home = (5, 'program', 1+3j)

# Dictionary is a data type that stores unordered data
# used to store a key - value pair
car = {"brand" : "benz", "model" : 2022, "color" : "silver"}
car1 = {"brand" : "bmw", "model" : 2021, "color" : "blue"}

print(car1["brand"])
print(car1["model"])


class FunEvent:
    def __init__(self, tags, year):
        self.tags = tags
        self.year = year 

    def __str__(self):
        return f"FunEvent(tags={self.tags}, years={self.year})"

tags = ["google", "ml"]
year = 2022
bootcamp = FunEvent(tags, year)

tags.append("bootcamp")
year = 2023
print(bootcamp)


# 16072022
# Conditions . also called Flow controls.
num = 0
if num > 0:
    print("num is a postitive number")
elif num == 0:
    print("NUm is 0")
else:
    print("Num is negative")


if num >=  0:
    if num == 0:
        print("Zero")
    else:
        print("Positive Number")
else:
    print("Negative number")

s='rpartion function'
print(s.rpartition('on'))

# Loops - this keeps on performinig a specific conditions until the condition is fulfiled
# for Loop

numbers = [6, 5, 3, 6, 7, 8, 12]
sum = 0

for item in numbers:
    sum += item

print("The sum is: " , sum)

# while Loop
val = 10
i = 1
sum1 = 0

while i <= val:
    sum1 += i 
    i += 1
    print(type(sum1))
    print(sum1)

print(sum1) 

# Functions - a block of code that is independent and discreet, that performa a specific task.
# it helps to make code reusable and also make it clean and readable.
from datetime import date
import time

t = time.localtime()
# current_time = time.strftime("%H:%M:%S", t)
current_time1 = time.strftime("%H:%M:%S %I:%M %p", t)
print(current_time1)

def greet():
    '''A function to greet a user'''
    name = input('First name: ')
    print('Hello ' + name + ', How are you?')

# function calling or invoking a function
print(current_time1)
greet()


# modify the greet function to greet according to time
# first from the system and then from user.

# function for returning an absolute value
def absolute_value(num):
    
    if num >= 0:
        return num
    else:
        return -num

num = float(input("Enter a number: "))
print("The Absolute value of", num, 'is' , absolute_value(num))


# Virtual environments - creates a container for a project and keep each versions in that container to avoid conflicts
# which may arise as a result of the different versions of the components
'''
PIP - is a package manager
pip --version
pip list  - show all packages installed
pip freeze

pip install virtualenv  - installing virtualenv

virtualenv hibreepy - creating a virtual environment called hibreedpy
hibreedpy\scripts\activate - to activate the virtualenv
deactivate - to deactivate the environment

git - version control software that helps us to keep changes
github - an online version of git
a repository - a store or folder that has been initialized as a git folder.

git init - git initialize repo
git status - the statius of my current files 
git add . - add every file at once to the git folder
git add file - adding a file to the git folder
git commit - m "add comment " - commiting the file to git
git remote -v

git rm --cached Bobby_Python_Tutorial_for_Beginners/python-course-for-beginners

git remote add origin https://github.com/superdalton/hibreed_python_lesson.git 
NB: origin can be anything, it is just an alias

git branch -M main 
NB: Git has branches, and can be created. Main was previously called Master, but not anymore. 
your local repository will contain main branch

git push origin main
'''

# draw a rectangle
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


# 
x = float(input("Enter value for x: "))

# Write your code here.
y = 1/ (x + 1/(x + 1/((x + 1/x))))

print("y =", y)

# 23072022
