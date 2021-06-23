################################################################################
# 標準ライブラリ
"""
よく使われるライブラリで Python で予め定義しているもの
import して利用する
https://docs.python.org/ja/3/library/index.html
"""


################################################################################
# datetime
"""
datetime の説明
https://docs.python.org/ja/3/library/datetime.html?highlight=datetime#module-datetime

出力形式指定時の指定子の種類
https://docs.python.org/ja/3/library/datetime.html?highlight=datetime#strftime-strptime-behavior
"""
import datetime

# 現在日時
now = datetime.datetime.now()
print(now)
# ISOフォーマット
print(now.isoformat())
# 独自に指定した形式
print(now.strftime('%Y/%m/%d-%H_%M_%S_%f'))

# 現在日（年月日のみ）
today = datetime.date.today()
print(today)
# ISOフォーマット
print(today.isoformat())
# 独自に指定した形式
print(today.strftime('%Y/%m/%d'))

# 時間（時分秒ミリ秒のみ）
# 引数で指定した時間を表す
t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
# ISOフォーマット
print(t.isoformat())
# 独自に指定した形式
print(t.strftime('%H_%M_%S_%f'))

# タイムデルタ（期間を表す）
# 1週間の期間
d = datetime.timedelta(weeks=1)
# 1週間前の日時
print(now - d)


################################################################################
# time
"""
time の説明
https://docs.python.org/ja/3/library/time.html?highlight=time#module-time
"""
import time

# 指定秒スリープ
print('###')
time.sleep(3)
print('###')
