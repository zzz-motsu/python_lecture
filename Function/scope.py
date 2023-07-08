def print_name_local():
    first_name = "Taro"
    last_name = "Yamada"
    print(f"I'm {first_name} {last_name}")


print_name_local()
# print(first_name)

# global変数（モジュール変数）
age = 30


# def print_age():
#     # age = 20 # local変数
#     print(f"I'm {age} year old")
#

# def print_age():
#     age = 20 # local変数
#     print(f"I'm {age} year old")

def print_age():
    global age
    age = 20
    print(f"I'm {age} year old")

print_age()
print(age)

