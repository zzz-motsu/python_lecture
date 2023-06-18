# input(): ユーザの入力した値を（文字列）を取得する

# age = input("何歳ですか？")
# print(f"あなたは{age}歳です")

user_age = int(input("何歳ですか？"))
casino_age = 20
game_text = """プレイするゲームの番号を選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
"""

if user_age >= casino_age:
    print("いらっしゃいませ")
    game = int(input(game_text))
    if game == 1:
        print("あなたはルーレットを選択しました")
    elif game == 2:
        print("あなたはブラックジャックを選択しました")
    elif game == 3:
        print("あなたはポーカーを選択しました")
    else:
        print("1~3を選択してください")

else:
    print(f"お客様は{casino_age}歳未満のため、カジノへは入店いただけません")