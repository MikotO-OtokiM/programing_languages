################################################################################
# 関数の定義
def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

# tomato が出力
result = what_is_this('red')
print(result)

# green pepper が出力
result = what_is_this('green')
print(result)

# I don't know が出力
result = what_is_this('yellow')
print(result)


################################################################################
# 位置引数、キーワード引数、デフォルト引数
def menu(main, drink, dessert):
    print(main)
    print(drink)
    print(dessert)

# 位置引数
# 関数定義で指定された引数の順番通りに引数を指定
menu('pasta', 'wine', 'ice')

# キーワード引数
# 指定する引数の順番は関数定義と違ってもよい
menu(drink='wine', dessert='ice',main='pasta')
# 位置引数との組み合わせも可能
# ただし、位置引数を利用する場所は関数定義と同じにする必要あり
menu('pasta', dessert='ice', drink='wine')

# デフォルト引数

def menu_defhikisu(main='beef',drink='watar', dessert='cake'):
    print(main)
    print(drink)
    print(dessert)

# 引数指定しない場合、デフォルト引数で定義した引数で実行される
menu_defhikisu()
# 以下のように表示される
"""
beef
watar
cake
"""

# 引数を指定した場合は、指定した引数にて実行される
menu_defhikisu('chicken')
# 以下のように表示される
"""
chicken
watar
cake
"""

# デフォルト引数利用時の注意
"""
    デフォルト引数に参照渡しのデータ型（リスト、辞書型など）は利用しない方がよい
    → 該当メソッドを複数回実行したときの実行結果が直感的に分かりづらくなるため
"""
def test_func(x, l=[]):
    l.append(x)
    return l

# 1 回目と2 回目で結果が異なる
# デフォルト引数である空のリストに対し、メソッドを実行したとき、直感的には
# 実行時に指定した引数のみが表示されるように感じるが、
# その前の実行結果に対して追加された結果になる。
r = test_func(100)
print(r)
r = test_func(100)
print(r)
# 以下のように表示される
"""
[100]
[100, 100]
"""


################################################################################
# 位置引数のタプル化
# * を引数の先頭に付けることで、その引数をタプル形式の引数として扱える
def say_something(word, *args):
    print('word:', word)
    for arg in args:
        print(arg)

# 第一引数が word に、第二引数以降が *args にタプル形式で設定され実行
say_something('Hi!', 'Mike', 'Nance')
# 以下のように表示される
"""
word: Hi!
Mike
Nance
"""


################################################################################
# キーワード引数の辞書化
# ** を引数の先頭に付けることで、その引数を辞書形式の引数として扱える
def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

# 指定したキーワード引数が辞書型データとして渡され実行される
menu(main='pasta', drink='wine')
# 以下のように表示される
"""
{'main': 'pasta', 'drink': 'wine'}
main pasta
drink wine
"""

# 予め辞書型データを定義しておき、渡すことも可能
d = {
    'main': 'chicken',
    'drink': 'beer'
}
# 引数が辞書型であることを示すために ** を引数の先頭に付加して実行
menu(**d)
# 以下のように表示される
"""
{'main': 'chicken', 'drink': 'beer'}
main chicken
drink beer
"""


################################################################################
# 関数内関数（インナー関数）
# 該当の関数の中だけで繰り返し実行する処理がある場合に利用
def outer(a, b):
    print('a:',a, 'b:', b)
    # 繰り返し実行する処理を関数内関数で定義
    def inner(c, d):
        return c + d
    # 定義した関数内関数を実行
    r1 = inner(a, b)
    r2 = inner(b, a)

    print(r1 + r2)
    return None

outer(1, 2)


################################################################################
# クロージャー
# 関数内関数の高度な使い方
"""
同じ処理を異なる条件で実行したい場合に利用
実行時に渡す引数が同じでも、実行結果が変わる
条件ごとに変えたい値（初期値）を外側の関数の引数として定義する
実際に実行したい処理を関数内関数として定義する
"""
# 例）円の面積を円周率の値を変えて計算する
# 円周率（pi）を初期値として外側の関数の引数とする
def circle_area_func(pi):
    # 関数内関数（実際に処理したい関数）を定義する
    def circle_area(radius):
        return radius * radius * pi
    # 外側の関数の戻り値として、関数内関数のアドレスを指定
    return circle_area

# 円周率を 3 で計算する場合の初期値（円周率）を設定
# ca1 には pi に 3 が設定された状態の circle_area のアドレスが設定される
ca1 = circle_area_func(3)
# 円周率を 3.14 で計算する場合の初期値（円周率）を設定
# ca1 には pi に 3.14 が設定された状態の circle_area のアドレスが設定される
ca2 = circle_area_func(3.14)

# 半径を指定し、異なる円周率での計算結果（関数内関数の処理結果）を表示
# 実行時に渡す引数（半径）が同じでも、事前に設定した円周率に従った異なる値が得られる
print(ca1(5))
print(ca2(5))
# 以下のように表示される
"""
75
78.5
"""


################################################################################
# デコレーター
# 関数内関数の高度な使い方
"""
クロージャーの初期値（実行時に変えたい異なる条件）が関数となる場合のこと
実行したい処理の前後に、必ず実行したい固定の処理を実行したい場合に利用
必ず実行したい処理と実行時に実行したい処理を関数内関数として定義する
"""
# 例）関数実行の前後に固定文字列（ログなど）を必ず表示する
# 実行時に実行したい処理を外側の関数の引数とする
def print_log(func):
    # 関数内関数（必ず実行したい処理と実行時に実行したい関数）を定義
    def wrapper(*args, **kwargs):
        # 必ず実行したい処理（実行時に実行する関数のログ）を記載
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        # 実行時に実行したい処理（外側の関数の引数として渡された関数）を記載
        func(*args, **kwargs)
        return None
    # 外側の関数の戻り値として、関数内関数のアドレスを指定
    return wrapper

# デコレーター（@を利用した記載）を用いて以降に定義した関数を（print_logに）渡す
@print_log
# 実行時に処理する関数を定義
def minus(a, b):
    print(a - b)
    return None
# 実行したい関数の引数を指定して実行
minus(10, 5)
# 以下のように表示される
"""
func: minus
args: (10, 5)
kwargs: {}
5
"""

# デコレーターを利用しない場合の記載（記載が煩雑になる）
"""
def minus(a, b):
    print(a - b)
    return None
# 実行したい関数を引数として指定し、f に関数内関数のアドレスを代入
f = print_log(minus)
# 実行したい関数の引数を指定して実行
f(10, 5)
"""


################################################################################
# ラムダ
# リストの要素編集など、特定の処理を実施したいが、わざわざ関数を定義するとコード量が
# 多くなってしまうようなケースで利用
# 例）リストの要素の先頭を大文字にする
l = ['Mon', 'tue', 'Wed', 'thu', 'fri', 'Sat', 'sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# lambdaを利用しない場合の書き方
# def sample_func(w):
#     return w.capitalize()

# lambdaを利用した書き方
sample_func = lambda w: w.capitalize()

change_words(l, sample_func)

# 引数として渡すときに直接 lambda で記載することも可能
# change_words(l, lambda w: w.capitalize())

# 以下のように表示される
"""
Mon
Tue
Wed
Thu
Fri
Sat
Sun
"""

# 例）個人別の点数のタプルのリストを、点数順にソート
score = [("Adam", 64), ("Bob", 82), ("Charlie", 21), ("David", 91)]
# タプルの2番目の要素をキーとしてソート
score.sort(key=lambda x: x[1])
print(score)
# 以下のように表示される
"""
[('Charlie', 21), ('Adam', 64), ('Bob', 82), ('David', 91)]
"""


################################################################################
# ジェネレーター
# 関数の return を yield に置き換えたもの
# yield 文で記載された要素を順に生成し返す
# 以下のようなケースで利用する
# ・無限に繰り返すイテレーション（繰返し処理）
# ・要素すべてをあらかじめ用意するのが計算コスト/メモリ使用量などの面で高負荷
def greeting():
    yield 'Good morning'
    # 例えば、要素を取得する処理の間に、以下のような高負荷な処理がある場合
    # 一度に要素を取得するとコストがかかってしまう
    # 高負荷の処理を1つの要素を取得するタイミングで実施させることで、
    # コストを分散させることができる
    # for i in range(1000000):
    #     print(i)
    yield 'Good afternoon'
    yield 'Good night'

# ジェネレーターを生成する
g = greeting()

# 要素を一つずつ生成する
print(next(g))
print(next(g))
print(next(g))
# 以下のように表示される
"""
Good morning
Good afternoon
Good night
"""


################################################################################
# ジェネレーター内包表記
# ジェネレーターを簡潔に高速に生成する方法
# 通常のジェネレーター生成
def g():
    for i in range(5):
        yield i

g = g()
for x in g:
    print(x)
# 以下のように表示される
"""
0
1
2
3
4
"""

# リスト内包表記でのリスト生成
g = (i for i in range(5))
for x in g:
    print(x)
# 以下のように表示される
"""
0
1
2
3
4
"""

# if 文で条件を指定可能
g = (i for i in range(5) if i % 2 == 0)
for x in g:
    print(x)
# 以下のように表示される
"""
0
2
4
"""