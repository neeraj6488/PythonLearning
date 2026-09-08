# try:
#     number = float(input("Enter a valid number: "))
#     print("Sum of 100 + {} = {}".format(number, 100 + number))
#     print("The block completed successfully")
# except:
#     print("Please enter a vaild number")


def add_numbers(num1, num2):
    """
    Args
    num1 (int): first number:
    num2 (int): second number:
    return:
    sum (int): sum of numbers
    """
    return num1 + num2


result = add_numbers(10, 20)
print("The sum of 10 and 20 is {}".format(result))
