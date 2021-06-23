################################################################################
# ファイル操作

################################################################################
# ファイルのオープン
"""
操作したいファイルを開き、ストリームを返す。失敗時に OSError を発生

open(file, mode='r', buffering=-1, encoding=None, errors=None,
           newline=None, closefd=True, opener=None
    )

modeの種類
    'r' 読み取り用にオープン (デフォルト)
    'x' 新しいファイルを作成し、書き込み用に開く
    'w' 書き込み用に開く※指定したファイルが存在する場合、基の情報は削除される
    'a' 書き込み用に開く※指定したファイルが存在する場合、基の情報の後に追加する
    'b' バイナリ モード
    't' テキストモード (デフォルト)
    '+' 更新用にディスク ファイルを開く (読み取りと書き込み)
    'U' ユニバーサル改行モード (非推奨)
"""
# Test と Hello World が書き込まれたファイルができる
f = open('files/20_test_file.txt', mode='w')
f.write('Test\n')
# print 関数に file= でファイルを渡し書き込むこともできるが、write を用いるのが一般的
print('Hello', 'World', file=f)
f.close()

# 読み込み（全てを読み込む）
f = open('files/20_test_file.txt', mode='r')
print(f.read())
f.close()

# 読み込み（1行ずつ読み込む）
f = open('files/20_test_file.txt', mode='r')
while True:
    line = f.readline()
    # readline で改行が入るため、print で end='' を設定する
    print(line, end='')
    if not line:
        break
f.close()

# 読み込み（チャンクごとに読み込む）
f = open('files/20_test_file.txt', mode='r')
while True:
    # チャンク（何文字ずつ読むか）を指定
    chunk = 2
    line = f.read(chunk)
    print(line)
    if not line:
        break
f.close()

# 読み込み（seek を使って読み込む）
f = open('files/20_test_file.txt', mode='r')
# 現在の位置を確認（先頭にカーソルがある状態なので 0 ）
# その位置から1文字読み込む
print(f.tell())
print(f.read(1))
# カーソルを 6 番目に移動し、2文字読み込む
f.seek(6)
print(f.read(2))
f.close()

# 読み込み＆書き込み
# mode で + を追加指定
f = open('files/20_test_file.txt', mode='r+')
print(f.read())
# 上の f.read() でカーソルが最後にきている状態
# 末尾に文字列を追加
f.write('Add Test\n')
# 文字列が追加され、カーソルが最後にきている状態
# 先頭にカーソルを戻す
f.seek(0)
# 文字列追加後の全体を出力
print(f.read())


################################################################################
# with ステートメントを用いたファイルのオープン
"""
with ステートメントを用いると、ファイルの close が不要
ファイルの閉じ忘れを防ぐことができる

with open(～) as f:
    ～～
"""
# 20_test_file.txt に追記
with open('files/20_test_file.txt', mode='a', encoding='utf-8') as f:
    f.write('##########\n')
    f.write('with ステートメントで追加\n')


################################################################################
# テンプレートの利用
"""
テンプレートを利用することで、テンプレートの一部のみを変えて利用することができる
開発者とデザイナーで分担して作業する場合などに、分業しやすい（HTMLなど）
"""
import string
with open('files/20_email_template.txt', mode='r') as f:
    # 読み込んだファイルをテンプレートに指定
    t = string.Template(f.read())
# テンプレート内のパラメータの値を指定してオブジェクトを作成
email = t.substitute(name='Mike', contents='How are you?')
print(email)
# 20_email_template.txt の中身
"""
Hi $name.

$contents

Have a good day.
"""
# 以下のように表示される
"""
Hi Mike.

How are you?

Have a good day.
"""


################################################################################
# CSVファイルへの書き込み
import csv
# ファイルオープンの際、Windows の場合は newline='' を指定する
# 改行が \r\n となり、読み込み時に2行改行されてしまうため
with open('files/20_test.csv', mode='w', newline='') as csv_file:
    # 見出し項目を指定
    title = ['Name', 'Count']
    # ファイルと見出し項目を指定し、ライターを作成
    writer = csv.DictWriter(csv_file, fieldnames=title)
    # 見出し行（ヘッダー）を書き込む
    writer.writeheader()
    # 行を書き込む
    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})


################################################################################
# CSVファイルへの読み込み
with open('files/20_test.csv', mode='r') as csv_file:
    # ファイルを指定しリーダーを作成
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])


################################################################################
# その他の操作（os ライブラリ）
import os

# 現在のディレクトリを確認する
print(os.getcwd())

# 指定したものの存在を確認する
print(os.path.exists('files/20_test_file.txt'))

# 指定したものがファイルかどうかを確認する
print(os.path.isfile('files/20_test_file.txt'))

# 指定したものがディレクトリかどうかを確認する
print(os.path.isdir('files/20_test_file.txt'))
print(os.path.isdir('sample_package'))

# ディレクトリを作成する
os.mkdir('files/test_dir')

# ディレクトリを削除する（ディレクトリ内が空でないと削除できない）
os.rmdir('files/test_dir')

# ディレクトリ内をリストを取得する
print(os.listdir('sample_package'))


################################################################################
# その他の操作（pathlib ライブラリ）
import pathlib
# 空のファイルを作成する
pathlib.Path('files/empty_file.txt').touch()

# ファイルを削除する
os.remove('files/empty_file.txt')


################################################################################
# その他の操作（その他 ライブラリ）
"""
他にもglob, shutil など、ファイル操作に便利はライブラリがある
"""
