################################################################################
# ロギング
"""
ログのレベル階層は以下の通り
    CRITICAL
    ERROR
    WARNING
    INFO
    DEBUG
"""
import logging

# コンソールにログを出力する場合
logging.basicConfig(level=logging.INFO)

# ファイルにログを出力する場合（filename= で出力先ファイルを指定）
# logging.basicConfig(filename='files/30_logging.log', level=logging.INFO)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')
# 以下のように表示される（指定したログレベル以上のログが出力）
"""
CRITICAL:root:critical
ERROR:root:error
WARNING:root:warning
INFO:root:info
"""

# 出力情報の追加
# フォーマッタを利用
logging.info('info {}'.format('test'))
# 以下のように表示される
"""
INFO:root:info test
"""

# %s を利用（Python2 からの方法）
logging.info('info %s' % ('test'))
# 以下のように表示される
"""
INFO:root:info test
"""

# ロギングの場合、カンマで区切って情報を指定可能
logging.info('info %s', 'test')
# 以下のように表示される
"""
INFO:root:info test
"""