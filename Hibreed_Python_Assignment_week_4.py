


'''2. Write pseudo algorithm for a shopping process on an e-commerce website.'''
'''
1. Search for the item to buy on the e-commerce website.
2. When found, add the item/product to cart/basket
3. Continue shopping, if there are more items.
4. if done shopping, check out 
5. Create an account before you buy, if not already have one.
6. finalize checkout adding all billing information and delivery address
7. pay for the item, using the available means (POD, Bank Transfer, Credit card etc)
8. Wait for the item to be delivered on the due date.
'''

'''3. Write a function that uses exception handling (try, except, finally).'''


def divide(x, y):
    try:
        print(f'{x}/{y} is {x / y}')
    except ZeroDivisionError as e:
        print(e, ". Do not divide by zero!")
    finally:
        print("Great Job")

divide(4,0)

'''4. Write a function that uses exception handling using at least three in-built exceptions. 
(try, except, finally)
'''     

def divide():
    try:
        x = float(input("enter Dividend: "))
        y = float(input("enter Divisor: "))

        print(f'{x}/{y} is {x / y}')

    except ZeroDivisionError as e:  # when you divide by 0
        print(e, ". Do not divide by zero!")
    
    except TypeError as e:
        print(e,". Can't divide different types of values")

    except ValueError as e:  # when you enter a string or character
        print(e, ". One of the values is not a number")

    finally:
        print("Great Job!!!")

divide()