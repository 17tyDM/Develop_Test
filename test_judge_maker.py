## テスト
import random
from judge_maker import make_judge

def test_make_judge_no1():
    """
    マトリックスNo：No1
    テスト内容：10点より下の点数がある場合
    """
    grade = "A"
    points = [100, 100, 100, 100, 100, 100, 100, 100, 100, 9]
    result = make_judge(grade, points)
    assert result == 3

def test_make_judge_no2():
    """
    マトリックスNo：No2
    テスト内容：30点以下の点数が3回以上ある場合
    """
    grade = "A"
    points = [100, 100, 100, 100, 100, 100, 100, 30, 30, 30]
    result = make_judge(grade, points)
    assert result == 2

def test_make_judge_no3_A():
    """
    マトリックスNo：No3
    テスト内容：成績が「A」の場合
    """
    grade = "A"
    points = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    result = make_judge(grade, points)
    assert result == 1

def test_make_judge_no3_B():
    """
    マトリックスNo：No3
    テスト内容：成績が「B」の場合
    """
    grade = "B"
    points = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    result = make_judge(grade, points)
    assert result == 1

def test_make_judge_no3_C():
    """
    マトリックスNo：No3
    テスト内容：成績が「C」の場合
    """
    grade = "C"
    points = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    result = make_judge(grade, points)
    assert result == 1

def test_make_judge_no4():
    """
    マトリックスNo：No4
    テスト内容：成績が「D」の場合
    """
    grade = "D"
    points = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    result = make_judge(grade, points)
    assert result == 2

def test_make_judge_no5():
    """
    マトリックスNo：No5
    テスト内容：成績が「E」の場合
    """
    grade = "E"
    points = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    result = make_judge(grade, points)
    assert result == 3

test_make_judge_no1()


# # 成績の指定
# grade = input("成績を入力してください。(英字[A-E])：").upper()
# # points のランダム生成
# #points = [random.randint(0, 100) for _ in range(10)]

# user_input = input("半角スペースで区切られた数値を入力してください：")
# points = list(map(int, user_input.split()))

# # 表示処理
# print(f"成績:{grade}")
# print(f"点数:{points}")
# # 実行
# result = make_judge(grade, points)
# # 結果出力
# print(result)