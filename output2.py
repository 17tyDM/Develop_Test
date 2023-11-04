import pandas as pd

# 科目番号と科目名の対応辞書
subject_mapping = {1: '国語', 2: '数学', 3: '理科', 4: '社会', 5: '英語'}

# CSVファイルを読み込む
df = pd.read_csv('input2.csv', header=None, names=['生徒番号', '科目番号', '点数'])

# 科目番号を科目名に変換
df['科目名'] = df['科目番号'].map(subject_mapping)

# 生徒番号ごとに科目別の合計、平均を計算
subject_totals = df.groupby(['生徒番号', '科目名'])['点数'].sum().unstack()
subject_means = df.groupby(['生徒番号', '科目名'])['点数'].mean().unstack()

# 生徒間での平均点の順位を計算
student_rank = subject_means.mean(axis=1).rank(ascending=True).astype(int)

# 生徒番号ごとに成績と判定を計算
student_summary = {}
for student_id, rank in zip(subject_totals.index, student_rank):
    grades = []
    judgments = []
    
    for subject in subject_totals.columns:
        total = subject_totals.loc[student_id][subject]
        mean = subject_means.loc[student_id][subject]
        
        # 順位から成績を決定
        if rank == 1:
            grade = 'A'
        elif rank <= 3:
            grade = 'B'
        elif rank <= 7:
            grade = 'C'
        elif rank <= 9:
            grade = 'D'
        else:
            grade = 'E'

        # 判定を初期化
        judgment = '合格'

        # 判定の条件分岐
        if (total <= 30).sum() >= 3 or grade in ('D'):
            judgment = '再テスト'
        elif (mean < 10).any() or grade in ('E'):
            judgment = '不合格'

        grades.append(grade)
        judgments.append(judgment)

    student_summary[student_id] = {subject: [total, mean, rank, grade, judgment] for subject, total, mean, grade, judgment in zip(subject_totals.columns, subject_totals.loc[student_id], subject_means.loc[student_id], grades, judgments)}

# 生徒番号ごとに成績と判定を出力
for student_id, subjects in student_summary.items():
    print(f'生徒番号:{student_id} - {subjects}')
