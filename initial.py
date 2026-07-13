try:
    answer=10/0
    number=int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError as err:
    print(err)