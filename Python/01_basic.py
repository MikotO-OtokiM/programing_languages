################################################################################
# 変数宣言（型指定は不要）
num = 1
name = 'Mike'
is_ok = True

print(num)
print(name)
print(is_ok)

# 変数をtype()で出力すると、引数のデータ型が分かる
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

# 型変換
str_num = '1'
#str から int へ変換
int_num = int(str_num)
print(int_num, type(int_num))


################################################################################
# printによる出力
print('Hi')
# 引数を複数指定すると、半角スペース区切りで出力される
print('Hi', 'Mike')
# sep で区切り文字を指定できる
print('Hi', 'Mike', sep = ',')
# end で末尾を指定できる（デフォルトは'\n'（改行）となっている）
# 1行目の末尾が空文字のため、連続して出力される
print('Hi', 'Mike', sep = ',', end = '')
print('Hi', 'Mike', sep = ',')


################################################################################
# 四則演算
# 掛け算
# 通常の掛け算（25）
print(5 * 5)
# べき乗（5 × 5 で 25）
print(5 ** 2)

# 割り算
# 通常の割り算（5.666666666666667）
print(17 / 3)
# 商のみ（5）
print(17 // 3)
# 余り（2）
print(17 % 3)
# round() の第二引数で小数点以下何桁でまるめるか指定できる（5.67）
print(round(17 / 3, 2))

# math関数
import math
# 平方根（5.0）
print(math.sqrt(25))
# 対数関数（3.321928094887362）
print(math.log2(10))


################################################################################
# 文字列
# 文字列は ' で囲む
print('Hello')
# " で囲むことも可能
print("Hello")
# " で囲むと文字列内の' は文字とみなされる
print("I don't know")
# ' で文字列を囲う場合は、文字列内の ' は \ でエスケープ
print('I don\'t konw')
# ' で文字列を囲う場合は、文字列内の ' は \ でエスケープ
print('say "I don\'t know"')
# " で文字列を囲う場合は、文字列内の " は \ でエスケープ
print("say \"I don't know\"")
# 文字列は自動で連結される
print('Hi.''Mike.')
# + で明示的に連結も可能
print('Hi.' + 'Mike.')

# 改行したい場合は \n を入れる
print('Hello.\nHow are you?')
# \n を改行として扱いたくない場合は r（rowデータを意味する）を先頭に付加
print(r'C:\name\name')

# 文字列（複数行）　" 3つで囲む
# 前後の改行をなくしたい場合は 以下のように \ を付加する
print("""\
line1
line2
line3\
""")

# 長い文字列を変数に指定する場合
# 自動で連結されることを利用し、長い文字列は複数行で記載すると見やすい
s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

# 文字列のインデックス、スライス
word = 'phthon'
# インデックス（0からスタート）
# 1文字目（p）
print(word[0])
# 2文字目（h）
print(word[1])
# 最後の文字（n）
print(word[-1])

# スライス
# 1～2文字目まで（ph）
print(word[0:2])
# 上の省略記載（ph）
print(word[:2])
# 2文字目以降（thon）
print(word[2:])
# 全ての文字列
print(word[:])

# 文字列の長さ
print(len(word))

# 文字の代入
# {} に format で指定した文字列が代入される（a is test）
print('a is {}'.format('test'))
# 複数指定可能（a is 1 2 3）
print('a is {} {} {}'.format(1, 2, 3))
# 順番指定可能（a is 3 2 1）
print('a is {2} {1} {0}'.format(1, 2, 3))
# 変数も利用可能
print('a is {first} {second}'.format(first=1, second=2))

# 文字の代入（f-strings）（3.6 以降）
"""
    以下の方法で、上記の format を用いた方法と同様の文字の代入ができる
    a = 1
    b = 2
    c = 3
    print(f'a is {a} {b} {c}')
"""

# 文字列操作
# 0 埋め
str = '1234'
# zfill(n) n 桁になるように左 0 埋め（00001234）
print(str.zfill(8))

# 右寄せ（00001234）
print(str.rjust(8, '0'))

# 左寄せ（12340000）
print(str.ljust(8, '0'))

# 中央寄せ（00123400）
print(str.center(8, '0'))


################################################################################
# コマンドライン引数
"""
ターミナル（Windows PowerShellなど）でPythonスクリプトファイルを実行する際、
ファイル名の後に半角スペース区切りで引数を渡すことが可能
sys.argv にリスト要素として以下の順番で渡される
    実行スクリプトファイル名
    半角スペース区切りで記載した引数
"""
# > python 01_basic.py option1 option2  をターミナルで実行する
import sys
for arg in sys.argv:
    print(arg)
# 以下のように表示される
"""
01_basic.py
option1
option2
"""
