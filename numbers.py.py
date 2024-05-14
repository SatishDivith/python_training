numbers_x = [10,20,30,40,10]
numbers_y = [75,65,35,75,30]

def check_first_last_same(numbers):
    return numbers[0]==numbers[-1]

result = check_first_last_same(numbers_y)
print("first and last same", result)