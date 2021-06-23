################################################################################
# temp ファイル操作
"""
temp ファイルとは、一時的に作成されるファイルのこと
Python の実行後にそのファイルは削除される
圧縮したいファイルを一時的にまとめておきたい場合などに利用する
"""
import tempfile
# メモリ上での temp ファイル作成（ディレクトリには表示されない）
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# 一時的に実際のファイルを作成（ディレクトリに表示されるが処理後に自動削除）
with tempfile.NamedTemporaryFile(mode='w+') as t:
    # 参考：作成した temp ファイルのパス
    print(t.name)
    t.write('test')
    t.seek(0)
    print(t.read())
    # この時点ではディレクトリにファイルが存在しているが、次の print 処理後に自動削除
    print('#######')

# 一時的にディレクトリを作成
with tempfile.TemporaryDirectory() as td:
    print(td)
    # この時点ではディレクトリにフォルダが存在しているが、次の print 処理後に自動削除
    print('#######')
