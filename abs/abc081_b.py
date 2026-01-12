N = int(input())
line = list(map(int, input().split()))
kaisuu = 0
while all(x % 2 == 0 for x in line): # 「lineの中身が全部偶数」である限り！
    line = [x // 2 for x in line]
    kaisuu += 1
print(kaisuu)