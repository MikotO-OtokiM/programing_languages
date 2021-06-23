################################################################################
# __pychache__（コンパイルされたモジュール）を作成しないための指定
# git に登録したくないので作成しないよう設定
import sys
sys.dont_write_bytecode = True


################################################################################
# import 文と as
"""
import 文には大きく3つの書き方がある。推奨はⅱの方法
ⅰ）「import パッケージ名.スクリプト名」の形式で import する場合の書き方
    「パッケージ名.スクリプト名.」を先頭に付けることで関数を実行
import sample_package.utils
r = sample_package.utils.say_twice('hello')
※コードが長くなってしまう

ⅱ）「from パッケージ名 import スクリプト名」の形式で import する場合の書き方
    「スクリプト名.」を先頭に付けることで関数を実行
from sample_package import utils
r = utils.say_twice('hello')
※どのスクリプトの関数かが分かり、コードも短く記載できる

ⅲ）「from パッケージ名.スクリプト名 import 関数名」の形式で import する場合の書き方
    関数を直接実行
from sample_package.utils import say_twice
r = say_twice('hello')
※どのスクリプトの関数かが分かりづらくなり、可読性が下がる

import sample_package.utils as u
のように as を用いて別の名前を付けることもできるが、どのスクリプトの関数かが
分かりづらくなるため使わない方がよいとされる
"""
# おすすめの方法（上記のⅱの形式）
from sample_package import utils
r = utils.say_twice('hello')
# 以下のように表示される
"""
hello!hello!!
"""


################################################################################
# import 文の記載順
"""
複数の import 文を記載する場合、以下の単位でアルファベット順に記載する
※間に1行開ける

ⅰ）Python の標準ライブラリ
ⅱ）サードパーティ製ライブラリ
ⅲ）自作パッケージ
ⅳ）同フォルダのスクリプトファイル
"""


################################################################################
# ImportError の使い所
"""
以下のように、try - except 文で囲むことで、import しようとしたスクリプトが
存在しない場合に発生する ImportErro をキャッチして、他のスクリプトをインポートする
ことができる

try:
    from sample_package import utils
except ImportError:
    from sample_package.tools import utils

バージョンの違いなどで、インポートしたいスクリプトの場所が変わった場合等に対応できる
"""
