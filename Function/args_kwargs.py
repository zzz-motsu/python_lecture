# args
# print("hello", "world", "test")
def get_average(*args):
    num = len(args)
    print(num)
    print(type(args))
    if num == 0:
        return 0
    total = sum(args)
    print(total)
    return total / num


average = get_average(1, 2, 3, 4, 5, 6, 7, 8)
print(average)

# **kwargs
def kwargs_func(**kwargs):
    param1 = kwargs.get('param1', 1)
    param2 = kwargs.get('param2', 2)
    param3 = kwargs.get('param3', 3)

    print(f"param1: {param1}, param2: {param2}, param3: {param3}")
    print(kwargs)

kwargs_func(param1=1, param3=3, param4=100)