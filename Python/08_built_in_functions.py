################################################################################
# 組み込み関数
"""
関数定義や import なしで利用できる関数
よく使われる関数で Python で予め定義しているもの
https://docs.python.org/ja/3/library/functions.html
"""


################################################################################
# ソート
"""
sorted(iterable, key=None, reverse=False)
    イテラブルのすべてのアイテムを昇順で含む新しいリストを返す
    引数にキーを設定してソート順をカスタマイズできる（key=~~）
    引数に逆フラグを設定して結果を降順でリクエストできる（reverse=Ture）
"""
ranking = {
    'Tom': 100,
    'Mike': 82,
    'Nancy': 95
}

# 辞書のキー項目の昇順でソート
print(sorted(ranking))
# 以下のように表示される
"""
['Mike', 'Nancy', 'Tom']
"""

# 辞書のキー項目の降順でソート
print(sorted(ranking, reverse=True))
# 以下のように表示される
"""
['Tom', 'Nancy', 'Mike']
"""

# 点数の昇順でソート
print(sorted(ranking, key=ranking.get))
# 以下のように表示される
"""
['Mike', 'Nancy', 'Tom']
"""

# 点数の降順でソート
print(sorted(ranking, key=ranking.get, reverse=True))
# 以下のように表示される
"""
['Tom', 'Nancy', 'Mike']
"""

# オブジェクトのソート
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
sorted(student_objects, key=lambda student: student.age)