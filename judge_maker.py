def make_judge(grade:str, points:list[int])->int:
    if grade in ["A", "B", "C", "D", "E"] and len(points) == 10:
        # 評価「3」につながる処理
        if grade == "E" or min(points) < 10:
            return 3
        else:
            bellow31_count:int = 0
            for point in points:
                if point < 31:
                    bellow31_count += 1
            # 評価「2」につながる処理
            if grade == "D" or bellow31_count >= 3:
                return 2
            # 評価「1」につながる処理
            else:
                return 1
    elif grade not in ["A", "B", "C", "D", "E"]:
        raise Exception("graderにA～E以外の文字が入力されています")
    elif len(points) != 10:
        raise Exception("pointsには0~100の数値10個をリスト型を入力してください")
    else:
        raise Exception("正しく入力されていません。")
