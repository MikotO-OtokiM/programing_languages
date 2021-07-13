################################################################################
# ロギング
""" ★注意★
ここで記載するログ出力（ログの root でログを操作し出力する）は
もっとも基本的な方法であるが、実際は推奨されていない
※他のファイルのログ出力に影響を与えてしまうため
※複数モジュールを利用する場合や、複数の開発者がいる場合などの実際の実装では
　logger、handlerを利用した方法が推奨されている
"""
"""
https://docs.python.org/ja/3/library/logging.html
ログのレベル階層は以下の通り
    CRITICAL
    ERROR
    WARNING
    INFO
    DEBUG
"""
import logging

# フォーマッタを用いた LogRecord 属性の出力
"""
https://docs.python.org/ja/3/library/logging.html#logrecord-attributes
"""
formatter = '%(asctime)s:%(levelname)s - %(message)s'
# コンソールにログを出力する場合
logging.basicConfig(level=logging.INFO, format=formatter)

# ファイルにログを出力する場合（filename= で出力先ファイルを指定）
# logging.basicConfig(
#     filename='files/30_logging.log',
#     level=logging.INFO,
#     format=formatter
#     )

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')
# 以下のように表示される（指定したログレベル以上のログが出力）
"""
2021-06-28 17:17:49,751:CRITICAL - critical
2021-06-28 17:17:49,753:ERROR - error
2021-06-28 17:17:49,754:WARNING - warning
2021-06-28 17:17:49,754:INFO - info
"""

# 出力情報の追加
# フォーマッタを利用
logging.info('info {}'.format('test'))
# 以下のように表示される
"""
2021-06-28 17:17:49,755:INFO - info test
"""

# %s を利用（Python2 からの方法）
logging.info('info %s' % ('test'))
# 以下のように表示される
"""
2021-06-28 17:17:49,756:INFO - info test
"""

# ロギングの場合、カンマで区切って情報を指定可能
logging.info('info %s', 'test')
# 以下のように表示される
"""
2021-06-28 17:17:49,758:INFO - info test
"""