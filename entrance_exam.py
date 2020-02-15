
#3科の4/3倍と、4科の合計の点数のいい方を出力します。
sub=["国語","算数","理科","社会"]
score=0
sanka=0
for i in range(len(sub)):
    score+=int(input(sub[i]+"の点数を入力してください "))
    if sub[i]=="理科":
        sanka=score*4/3
if score<sanka:
    print("あなたの点数は "+str(round(sanka,2))+"点です。ちなみに、4科の点数は、"+str(score)+"点です。")#roundで小数を丸める
else:
    print("あなたの点数は "+str(score)+"点です。ちなみに、3科の4/3倍は、"+str(round(sanka,2))+"点です。")
"#Python_playing"
