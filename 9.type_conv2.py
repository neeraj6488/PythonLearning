try:
    number = float(input("Enter a valid number: "))
    print("Sum of 100 + {} = {}".format(number, 100 + number))
    print("The block completed successfully")
except:
    print("Please enter a vaild number")