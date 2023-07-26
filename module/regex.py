import re

# email = "myemail@gmail.com"
# matched = re.search('@\w+\.', email)
# if matched:
#     print(matched)
#     print("matched")
# else:
#     print("Matched")
#
#
# # metacharacter
# # []
# print(re.search('[abc]', 'a'))
# print(re.search('[a-c]', 'b'))
# print(re.search('[0-9]', 'b')) # None
# print(re.search('[0-9]', '3'))
# print(re.search('[0-9]', 'sgsdf3'))
#
# # ^ 最初の文字
# print(re.search('^[0-9]', '0test'))
# print(re.search('^[0-9]', 'test0')) # None
#
# # {} n回リピート：最初の文字からn番目が0-9の間であるか
# print(re.search('^[0-9]{4}', '2023/7/9'))
# print(re.search('^[0-9]{4}', '202f/7/9')) # None
#
# # {n,m} 最低n回、　最高n回リピート
# print(re.search('^[0-9]{2,4}', '23/7/9'))
# print(re.search('^[0-9]{2,4}', '2f/7/9')) # None
# print(re.search('^[0-9]{2,4}', '20d3/7/9'))
#
# # $ 最後の文字
# print(re.search('[0-9]{2}$', '2023/7/19'))
# print(re.search('[0-9]{2}$', '2023/7/9')) # None
#
# # * 左のパターンを0回以上繰り返す
# print(re.search('a*b', 'a')) # None
# print(re.search('a*b', 'b'))
# print(re.search('a*b', 'ab'))
# print(re.search('a*b', 'aaaaab'))
#
# # + 左のパターンを1回以上繰り返す
# print(re.search('a+b', 'b')) # None
# print(re.search('a+b', 'ab'))
# print(re.search('a+b', 'a')) # None
#
# # ? 左のパターンを0回か1回繰り返す
# print(re.search('ab?c', 'a')) # None
# print(re.search('ab?c', 'ab')) # None
# print(re.search('ab?c', 'bc')) # None
# print(re.search('ab?c', 'ac'))
# print(re.search('ab?c', 'abc'))
# print(re.search('ab?c', 'abbc')) # None
#
# # | or
# print(re.search('abc|012', 'abc'))
# print(re.search('abc|012', '012'))
# print(re.search('abc|012', '01')) # None
#
# # () グループ
# print(re.search('te(s|x)t', 'test'))
# print(re.search('te(s|x)t', 'text'))
# print(re.search('te(s|x)t', 'tent')) # None
#
# # . 任意の一文字
# print(re.search('h.t', 'hot'))
# print(re.search('h.t', 'hat'))
# print(re.search('h.t', 'ht')) # None
#
# # \ エスケープ 記号を文字列として認識させる
# print(re.search('h\.t', 'h.t'))
#
# # \w [a-zA-Z0-9_]すべてのアルファベット、数字及びアンダースコア
# print(re.search('h\wt', 'hgt'))
# print(re.search('h\wt', 'h1t'))
# print(re.search('h\wt', 'h-t')) # None
# print(re.search('h\wt', 'h_t'))


# challenge1
# patten_dob = "^(19|20)[0-9]{2}/([1-9]|1[0-2])/([1-9]|1[0-9]|2[0-9]|3[01])$"
# while True:
#     dob = input("生年月日を入力してください(yyy/mm/dd)")
#     result = re.search(patten_dob, dob)
#     if result:
#         print(f"{dob}は正しいフォーマットです")
#         break
#     else:
#         print(f"{dob}は正しくないフォーマットです")


# challenge2
patten_email = "^(\w|\.|-)+@(\w|\.|-)+\.[a-zA-Z]{2,3}$"
while True:
    email = input("emailを入力してください")
    result = re.search(patten_email, email)
    if result:
        print(f"{email}は正しいフォーマットです")
        break
    else:
        print(f"{email}は正しくないフォーマットです")
