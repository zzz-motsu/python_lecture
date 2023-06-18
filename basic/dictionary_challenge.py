user_age = int(input("何歳ですか？"))
casino_age = 20
# game_text = """プレイするゲームの番号を選択してください
# 1: ルーレット
# 2: ブラックジャック
# 3: ポーカー
# :
# """

game_dict = {'1': 'ルーレット', '2': 'ブラックジャック', '3': 'ポーカー', '4': 'スロット'}

if user_age >= casino_age:
    print("いらっしゃいませ")
    while True:
        print("プレイするゲームを選んでください.")
        for num, game_name in game_dict.items():
            print(f"{num}: {game_name}")
        game = input(":")
        if game in game_dict:
            print(f"あなたは{game_dict[game]}を選びました")
            break
        else:
            print("正しい選択肢を選んでください")
        # if game == 1:
        #     print("あなたはルーレットを選択しました")
        #     break
        # elif game == 2:
        #     print("あなたはブラックジャックを選択しました")
        #     break
        # elif game == 3:
        #     print("あなたはポーカーを選択しました")
        #     break
        # else:
        #     print("1~3を選択してください")

else:
    print(f"お客様は{casino_age}歳未満のため、カジノへは入店いただけません")