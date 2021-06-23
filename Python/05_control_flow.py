################################################################################
# if 文
x = 10
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

# 複数条件を判定する場合は and か or で条件を記載
a = 10
b = 20
if a > 0 and b > 0:
    print('a and b are positive')

if a > 0 or b > 0:
    print('a or b are positive')


################################################################################
# while 文と continue 文、break 文
count = 0
# 条件式が True の間繰り返す
while count < 10:
    if count > 7:
        print('break')
        # while 文を抜ける
        break
    if count == 2:
        count += 1
        print('continue')
        # 以降の処理は実施せず、繰り返し判定部分に戻る
        continue
    print(count)
    count += 1
# 以下のように表示される
"""
0
1
continue
3
4
5
6
7
break
"""

# while else 文
"""
    else 内の処理は while の条件式での繰り返しが終わった後に実行される
    break 文は else も含めた while 文全体を抜けることに注意
"""
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('Done')
# 以下のように表示される
"""
0
1
2
3
4
Done
"""


################################################################################
# while 文と input 関数
"""
input
    標準入力から文字列を読み取る。 末尾の改行は削除される
    引数に文字列が指定されている場合は、標準出力に出力される
    ユーザーがEOF（* nix：Ctrl-D、Windows：Ctrl-Z + Return）を押した場合は、
    EOFErrorを発生させる
"""
while True:
    # Enter: を標準出力に表示し、入力を待つ
    word = input('Enter:')
    if word == 'ok':
        # 入力された文字列が条件に該当したら break
        break
    print('next')


################################################################################
# for 文
"""
    while 文と同様、break 文、continue 文、else 文を利用可能
    _ を用いると、for 文内でイテレータ要素を利用しないことを明示的に表現できる
"""
some_list = [1, 2, 3, 4, 5]

# in でリストの要素を順番に取り出し処理を繰り返す
for i in some_list:
    print(i)
# 以下のように表示される
"""
1
2
3
4
5
"""

for _ in some_list:
    print('hello')
# 以下のように表示される
"""
hello
hello
hello
hello
hello
"""

for s in 'abcde':
    print(s)
# 以下のように表示される
"""
a
b
c
d
e
"""

################################################################################
# for 文と range 関数
"""
range
    指定範囲の整数のシーケンスを生成する
    range(start, stop[, step])
    range（i、j）は、i、i + 1、i + 2、...、j-1を生成する
    startのデフォルトは0で、stopは省略
    stepを指定すると、インクリメント（またはデクリメント）が指定される（飛び番を生成）
"""
for num in range(5):
    print(num)
# 以下のように表示される
"""
0
1
2
3
4
"""

for num in range(2,5):
    print(num)
# 以下のように表示される
"""
2
3
4
"""

for num in range(2,10, 3):
    print(num)
# 以下のように表示される
"""
2
5
8
"""


################################################################################
# for 文と enumerate 関数
"""
enumerate
    リストなどの要素のインデックスを作成し返す
"""
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)
# 以下のように表示される
"""
0 apple
1 banana
2 orange
"""


################################################################################
# for 文と zip 関数
"""
zip
    指定したリストなどの要素の最小数にて、各データの先頭からの要素を順に取得し
    タプルを作成する
    list（zip（ 'abcdefg'、range（3）、range（4）））
    [（ 'a'、0、0）、（ 'b'、1、1）、（ 'c'、2、2）]
"""
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)
# 以下のように表示される
"""
Mon apple coffee
Tue banana tea
Wed orange beer
"""


################################################################################
# for 文と items 関数
"""
items
    辞書型データのキーと値のリストのタプルを作成する
"""
d= {'x': 100, 'y': 200}

# dict_items([('x', 100), ('y', 200)])
print(d.items())

# k と v に items関数で戻されたキーと値のリストがアンパックされ設定される
for k, v in d.items():
    print(k, ':', v)
# 以下のように表示される
"""
x : 100
y : 200
"""


################################################################################
# 例外処理
l = [1, 2, 3]
i = 5

try:
    # 成功する処理
    # l[0]
    # 存在しないインデックスの参照　→　IndexError でキャッチ
    l[i]
    # できない処理（タプルの更新）　→　Excetion でキャッチ
    # () + l

# try 内の処理が失敗した場合のみ、実行される処理
# 例外の種類別に処理を分けることができる
except IndexError as e:
    print("Don't worry:{}".format(e))
except Exception as e:
    print("other:{}".format(e))
# try 内の処理が成功した場合のみ、実行される処理
else:
    print('Done')
# Exception が発生しても発生しなくても必ず実行される処理
finally:
    print('clean up')

# 例外処理した後の処理も実行される
print('last')

"""
例外クラスの階層
https://docs.python.org/ja/3.9/library/exceptions.html?highlight=exception#exception-hierarchy
"""


################################################################################
# 独自例外の作成
# 独自の例外クラスを定義
class UppercaseError(Exception):
    # 継承したクラス（Exception）の内容をそのまま引き継ぐ場合は pass を記載
    # 独自の処理を追加したい場合はここに記載することで追加可能
    pass

def check():
    words = ['APPLE', 'arange', 'banana']
    for word in words:
        # 全て大文字だったら
        if word.isupper():
            # 例外を発生させる
            raise UppercaseError(word)

try:
    check()
except UppercaseError as e:
    print('This is my fault', e)