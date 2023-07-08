# lambda関数（無名関数）

def square(x):
    return x * x

print(square(3))


lambda x: x * x

print(square(3))

# def power(exponent):
#     def inner_power(base):
#         return base ** exponent
#     return inner_power

def power(exponent):
    return lambda base:  base ** exponent


third_power = power(3)
print(third_power(2))

numbers = [6, 2, 5, 43, 5, 36, 67, 2]
# filter()

# def filterfunc(num):
#     if num % 2 == 0:
#         return False
#     else:
#         return True

# def filterfunc(num):
#     return not num % 2 == 0

# def filterfunc(num):
#     return num % 2

# filtered_num = filter(filterfunc, numbers)
filtered_num = filter(lambda num: num % 2, numbers)
print(filtered_num)
print(list(filtered_num))

# for num in numbers:
#     print(filterfunc(num))