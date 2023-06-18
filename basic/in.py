# in演算子
# fruits = ["apple", 'peach', 'grapes', 'banana']
# print('lemon' not in fruits)
# print('h' in 'hello')

fruits = input("好きなフルーツを入力してください")
fruits_list = ["apple", 'peach', 'grapes', 'banana']

if fruits in fruits_list:
    print(f"{fruits}ですね、差し上げます。")
    fruits_list.remove(fruits)
else:
    print("{fruits}ですね、仕入れました！")
    fruits_list.append(fruits)

print(f"残りのフルーツはこちらです。{fruits_list}")