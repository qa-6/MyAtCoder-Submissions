A, B, C, X = [int(input()) for _ in range(4)] # 4行分をスマートに読み込む

ans = 0
for i in range(A + 1):
    for j in range(B + 1):
        # 500円と100円で払った残りの金額
        nokori = X - (500 * i + 100 * j)
        
        # 残りが「0以上」かつ「50円で割り切れる」かつ「枚数がC枚以内」ならOK！
        if nokori >= 0 and nokori % 50 == 0 and (nokori // 50) <= C:
            ans += 1

print(ans)