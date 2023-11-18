def make_judge(grade, points):
    if grade == "E":
        return 3
    else:
        retest = 0
        for point in points:
            if point <= 10:
                return 3
            elif point <= 30:
                retest += 1
        if grade == "D" or retest >= 3:
            return 2

## テスト
# points の生成
import random
points = [random.randint(0, 100) for _ in range(10)]
# points の表示
print(points)
# 実行
result = make_judge("D", points)
# 結果出力
print(result)
