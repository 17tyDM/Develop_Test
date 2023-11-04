import pandas as pd

# 科目番号と科目名の対応辞書
subject_mapping = {1: '国語', 2: '数学', 3: '理科', 4: '社会', 5: '英語'}

# CSVファイルを読み込む
df = pd.read_csv('input2.csv', header=None, names=['生徒番号', '科目番号', '点数'])

# 科目番号を科目名に変換
df['科目名'] = df['科目番号'].map(subject_mapping)

# 生徒番号ごとに科目別の合計、平均、成績、判定を計算
student_summary = {}
for student_id, student_data in df.groupby('生徒番号'):
    subject_totals = student_data.groupby('科目名')['点数'].sum()
    subject_means = student_data.groupby('科目名')['点数'].mean()
    
    # 平均点を使って順位を計算
    rank = subject_means.rank(ascending=False).astype(int)
    
    grades = []
    judgments = []

    for subject, total, mean, r in zip(subject_totals.index, subject_totals, subject_means, rank):
        # 順位から成績を決定
        if r == 1:
            grade = 'A'
        elif r <= 3:
            grade = 'B'
        elif r <= 7:
            grade = 'C'
        elif r <= 9:
            grade = 'D'
        else:
            grade = 'E'

        # 判定を初期化
        judgment = '合格'

        # 成績がDまたはEの場合は再テストまたは不合格
        if grade in ('D', 'E'):
            judgment = '再テスト' if student_data[student_data['科目名'] == subject]['点数'].lt(30).sum() >= 3 else '不合格'

        grades.append(grade)
        judgments.append(judgment)

    student_summary[student_id] = {subject: [total, mean, r, grade, judgment] for subject, total, mean, r, grade, judgment in zip(subject_totals.index, subject_totals, subject_means, rank, grades, judgments)}

# 生徒番号ごとに成績と判定を出力
for student_id, subjects in student_summary.items():
    print(f'生徒番号:{student_id} - {subjects}')
