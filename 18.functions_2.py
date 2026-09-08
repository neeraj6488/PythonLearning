def process(numbers):
    total_sum = sum(numbers)
    average_num = total_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return(f"Total: {total_sum}, Average: {average_num}, Min: {minimum} , Max: {maximum}")

result = process([1, 2, 3, 4, 5])
print(result)

float_result = process([11,12.2,14.1])
print(float_result)