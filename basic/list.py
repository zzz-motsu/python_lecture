fruits = ['apple', 'peach', 'melon', 'grapes']

hetro_list = ['string', 1, 3, 4, True, fruits]
print(fruits)

# .append: 新しいオブジェクトを追加する
fruits.append('banana')
print(fruits)

# .insert: 指定したindexに指定したオブジェクトを追加する
fruits.insert(3, 'lemon')
print(fruits)

# .remove: マッチした最初のオブジェクトを除く
fruits.remove('peach')
print(fruits)

# .sort: 昇順に並び替える
fruits.sort()
print(fruits)
# 降順
fruits.sort(reverse=True)
print(fruits)

# len(): リストの要素数を取得する（length）
print(len(fruits))
print(len("hello world"))