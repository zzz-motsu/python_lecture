# forループ
fruits = ["apple", 'peach', 'grapes', 'banana']

# for fruit in fruits:
#     print(f"I love {fruit}!!")
#
# for char in "hello world!!":
#     print(f"char: {char}")

# iterationとiterable

# favorite = input("好きなフルーツは？")
# for fruit in fruits:
#     if fruit == favorite:
#         print(f"I love {fruit}!!")
#     else:
#         print(f"{fruit}は別に普通...")

favorite_fruits = []
normal_fruits = []
for fruit in fruits:
    choice = input(f"{fruit}は好き？ y/n")

    if choice == "y":
        favorite_fruits.append(fruit)
    else:
        normal_fruits.append(fruit)

print(f"favorite fruits: {favorite_fruits}")
print(f"normal fruits: {normal_fruits}")