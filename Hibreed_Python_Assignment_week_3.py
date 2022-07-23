'''
Module 3 assignment
1.	Iterate the given list of numbers and print only those numbers which are divisible by 5
Given list is:  number = [10, 20, 33, 46, 55, 62, 70]

2.	Write a function to Calculate income tax for the given income by adhering to the below rules
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20

If the taxable income is 45000, the income tax payable is?

3.	Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
Given 1:
number1 = 20
number2 = 30

Given 2:
number1 = 40
number2 = 30

4. Write a program to remove characters from a string starting from zero up to n and return a new string.

'''
# 1.	Iterate the given list of numbers and print only those numbers which are divisible by 5

number = [10, 20, 33, 46, 55, 62, 70]

for item in number:
    if item % 5 == 0:
        print(item)

# 2.	Write a function to Calculate income tax for the given income by adhering to the below rules
'''
if income <= 10000, then rate = 0
	tax = 0
if income <= 20000, then rate = 10% (0.1)
	tax = (income - 10000) *  0.1
if income > 20000, then rate = 20 (0.2)
	tax = (income - 20000) * 0.2 + (10000 * 0.1)
'''

'''Using the while statement to catch any error in the input from the user.
This is to ensure that the user enters an amount.'''
while True:
    try:
        income = float(input("Please enter your income amount: "))
        
    except ValueError:
        print("You did not enter an amount")
        
        continue

    else:
        break


'''A function to calculate the income tax according to the tax rules'''
def incomeTax(income):
    if income <= 10000:
        taxAmount = 0
        return taxAmount
    elif float(income) <= 20000:
        taxAmount = (income - 10000) * 0.1
        return taxAmount
    else:
        taxAmount = (income - 20000) * 0.2 + (10000 * 0.1)
        return taxAmount

tax = incomeTax(income)
print(f"For your income of NGN{income:.2f}, you are expected to pay a tax of NGN{tax:.2f}". format(income = income, tax = tax))



'''
3.	Given two integer numbers return their product only if the product is equal to or lower than 1000, 
else return their sum.
Given 1:
number1 = 20
number2 = 30

Given 2:
number1 = 40
number2 = 30
'''

'''Accept Integer input from the user'''
number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))


product = number1 * number2
sum = number1 + number2

if product <= 1000 :
    print(product) 
else:
    print(sum)


'''
4. Write a program to remove characters from a string starting from zero up to n and return a new string.
The function should be able to take in a string and an nth value
'''

'''A Function to accept a string from users and the positional value of the string to be removed. '''

def stringRemoval():
    choice_string = input("Enter your choice string: ")
    nth_value = int(input("Enter the position of the value to be removed: "))
    output_string = ""

    for i in range(0, len(choice_string)):  # For the range of strings entered by the user,
        if i != nth_value - 1:              # if i is not the value the user wants to remove
            output_string += choice_string[i]  #Continue to add the string to the output_string
    
    print(f"After removing the {nth_value}th letter from '{choice_string}', you are left with: {output_string} ".format(nth_value=nth_value, choice_string= choice_string, output_string = output_string ))


stringRemoval()
