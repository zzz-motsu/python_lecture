# whileループ
# count = 0
# while count < 10:
#     print(count)
#     count += 1
#
# # break と continue
# while True:
#     age = int(input("あなたは何歳ですか？"))
#     if not 0 <= age < 120:
#         print("入力された値は正しくありません")
#         continue
#     else:
#         print(f"あなたは{age}歳です")
#         break

user_age = int(input("何歳ですか？"))
casino_age = 20
game_text = """プレイするゲームの番号を選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
:
"""

if user_age >= casino_age:
    print("いらっしゃいませ")
    while True:
        game = int(input(game_text))
        if game == 1:
            print("あなたはルーレットを選択しました")
            break
        elif game == 2:
            print("あなたはブラックジャックを選択しました")
            break
        elif game == 3:
            print("あなたはポーカーを選択しました")
            break
        else:
            print("1~3を選択してください")

else:
    print(f"お客様は{casino_age}歳未満のため、カジノへは入店いただけません")