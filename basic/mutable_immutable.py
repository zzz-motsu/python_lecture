# mutable: 変更可能なオブジェクト list, dict, set
fruits = ['apple', 'peach', 'banana']
print(f"fruitsのIDは{id(fruits)}")
fruits.append('lemon')
print(fruits)
print(type(fruits))
print(f"fruitsのIDは{id(fruits)}")

# immutable: 変更不可能なオブジェクト int, froat, bool, tuple
fruit = 'aplle'
print(f"fruitのIDは{id(fruit)}")
print(type(fruit))
fruit += ', lemon'
print(fruit)
print(type(fruit))

# メモリを多く使用し非効率
text = "" # 1-2-3-4-5-6-7-8-9
for i in range(1, 11):
    if i == 1:
        text += str(i)
    else:
        text += "-" + str(i)
print(text)

# メモリを節約し効率的
text_list = []
for i in range(1, 11):
    text_list.append(str(i))

text = "-".join(text_list)
print(text)