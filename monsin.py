# 患者の問診をするプログラム

anxiey = input("最近の悩み事を聞かせてください:")
depression = input("今どのくらい憂鬱ですか。1から5までの数字で回答してください:")

with open("monsin.txt","w",encoding="utf-8") as f:
    f.write("患者が不安に思っていることは " + anxiey)
    f.write("\n")
    f.write("患者の憂鬱度は " + depression)

#depressionが数値じゃない場合の例外処理を書きたい

print("アンケートにご協力ありがとうございます。")
print("以下が問診票に記録されました。")

with open("monsin.txt","r",encoding="utf-8") as r:
    print(r.read())

print("発想を変えて、" + anxiey + "の悪くないところはなんだと思いますか？" + anxiey + "であることのメリットはなんだと思いますか？" )
cbt= input("以下に記入してみてください:")
depression = input("今どのくらい憂鬱ですか。1から5までの数字で回答してください:")

with open("monsin.txt","w",encoding="utf-8") as f:
    f.write("患者が不安に思っていることは " + anxiey)
    f.write("\n")
    f.write("患者の憂鬱度は " + depression)

print("少し憂鬱度に変化がありましたか？")
print("以下が問診票に記録されました。")

with open("monsin.txt","r",encoding="utf-8") as r:
    print(r.read())