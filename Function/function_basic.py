# 関数(function)

# 華氏から摂氏に変換する
fahrenheit = 72
# celsius = (fahrenheit - 32) * 5/9
# print(celsius)

def fahrenheit_to_celsius(a):
    b = (a - 32) * 5/9
    return b

celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius)