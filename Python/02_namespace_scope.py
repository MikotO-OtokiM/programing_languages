"""
グローバル変数の__doc__に格納される文字列
"""
################################################################################
# 名前空間とスコープ
animal = 'cat'

def f():
    # 下の行を有効にするとエラーになる
    # ローカル変数の animal を出力しようとするが、それを定義する前に呼び出している
    # と解釈されるため。
    # print(animal)

    animal = 'dog'
    print('local:', animal)
    print('ローカル変数', locals())

# ローカル変数の animal とローカル変数 が出力される
f()
# 以下のように表示される
"""
local: dog
ローカル変数 {'animal': 'dog'}
"""
# グローバル変数の animal とグローバル変数が出力される
print('global:', animal)
print('グローバル変数', globals())
# 以下のように表示される
"""
global: cat
グローバル変数 {
'__name__': '__main__',
'__doc__': '\nグローバル変数の__doc__に格納される文字列\n',
'__package__': None,
'__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x~~>,
'__spec__': None,
'__annotations__': {},
'__builtins__': <module 'builtins' (built-in)>,
'__file__': 'c:\\~~~\\Python\\02_namespace_scope.py',
'__cached__': None,
'animal': 'cat',
'f': <function f at 0x0000026BB8847160>}
"""


################################################################################
# 予め定義されているグローバル変数
# __name__
"""
__main__ はPythonが実行されたときに最初に実行されるスクリプトであることを示している
"""

# __doc__
"""
スクリプトファイルの先頭に記載したコメント文が格納される
該当のスクリプトファイルの説明を書いたりする
"""

