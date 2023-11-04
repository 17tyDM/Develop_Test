import pandas as pd

# 科目番号と科目名の対応辞書
subject_mapping = {1: '国語', 2: '数学', 3: '理科', 4: '社会', 5: '英語'}

# CSVファイルを読み込む
df = pd.read_csv('input2.csv', header=None, names=['生徒番号', '科目番号', '点数'])

# 科目番号を科目名に変換
df['科目名'] = df['科目番号'].map(subject_mapping)

# 生徒番号ごとに科目別の合計と平均を計算
result = df.groupby(['生徒番号', '科目名'])['点数'].agg(['sum', 'mean'])

# 生徒番号ごとに各科目の合計と平均をまとめる
student_summary = {}
for student_id, data in result.groupby('生徒番号'):
    student_data = {}
    for subject, scores in data.iterrows():
        subject_name = subject[1]
        student_data[subject_name] = [scores['sum'], scores['mean']]
    student_summary[student_id] = student_data

# 生徒番号ごとに各科目の合計と平均を出力
for student_id, subjects in student_summary.items():
    print(f'生徒番号:{student_id} - {subjects}')
