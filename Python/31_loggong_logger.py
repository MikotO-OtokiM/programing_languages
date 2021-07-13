################################################################################
# ロギング（ロガーを利用したログ出力）
"""
ログ出力はここで記載する logger、handler を利用する方法が推奨されている
logger の設定（handler や formatter など）を コンフィグを利用して指定することも可能
＜logging.config＞
https://docs.python.org/ja/3/library/logging.config.html
"""
import logging

# logger を作成する
# 自身のファイル名（ __name__ ）を引数に作成することが推奨されている
logger = logging.getLogger(__name__)

# handler を作成し、logger に設定する
# https://docs.python.org/ja/3/library/logging.handlers.html
# コンソールに出力する場合
streamhandler = logging.StreamHandler()
logger.addHandler(streamhandler)

# ファイルに出力する場合
# filehandler = logging.FileHandler()
# logger.addHandler(filehandler)



# ログレベルを設定する
logger.setLevel(logging.INFO)

logger.info('from main')


################################################################################
# ロギング（フィルタを利用したログ出力）
"""
特定の文字列が含まれるログを出力したくない場合に、フィルタを利用する
"""
# フィルタのクラスを定義する
class NoPassFilter(logging.Filter):
    # filter関数をオーバーライド
    def filter(self, record):
        log_message = record.getMessage()
        # 特定の文字列（例では password）がログに含まれているかの Boolean を返す
        return 'password' not in log_message

# 定義したフィルタのクラスをロガーに追加する
logger.addFilter(NoPassFilter())
logger.info('from main filter')
logger.info('from main filter password = test')
# 以下のように表示される（フィルタに該当するログは出力されない）
"""
from main filter
"""