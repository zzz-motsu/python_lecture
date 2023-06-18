# is演算子：同じオブジェクトかどうか判定する

a = 1
b = 1
c = 3
d = a
e = 2 - 1 # 1

print(id(a))
print(id(b))
print(id(c))
print(id(d))

print(a is b)
print(a is not c)
print(d is a)
print(a is e)

# Noneかどうかの判定によく使う

nothing = None
print(nothing is None)
print(id(nothing))
print(id(None))