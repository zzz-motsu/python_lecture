print("hello world!!")
print('1')

print("""
hello world!!
""")

print("hello \nworld!!")
print("hello \tworld!!")

print("back slash n:\\n")

print('I\'m fine')

print("hello" + "world" + "!!")


# format
hello = "hello"
world = "world"
mark = "!!"
print("{} {}{}".format(hello, world, mark))

name = "Emily"
print("Hey, {}!! How are you doing?".format(name))

balance = 100
print("balance: {}".format(balance))

print(type(balance))

# fstrings
print(f"Hey, {name}!! How are you doing?")
print(f"balance: {balance}")