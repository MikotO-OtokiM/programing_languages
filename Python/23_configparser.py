################################################################################
# config ファイル
"""
以下の形式で定義された設定ファイル
[Simple Values]
key=value
spaces in keys=allowed
spaces in values=allowed as well
spaces around the delimiter = obviously
you can also use : to delimit keys from values

[All Values Are Strings]
values like this: 1000000
or this: 3.14159265359
are they treated as numbers? : no
integers, floats and booleans are held as: strings
can use the API to get converted values directly: true

[Multiline Values]
chorus: I'm a lumberjack, and I'm okay
    I sleep all night and I work all day

[No Values]
key_without_value
empty string value here =

[You can use comments]
# like this

https://docs.python.org/ja/3/library/configparser.html?highlight=config#supported-ini-file-structure
"""

import configparser

# ConfigParser オブジェクト作成
config = configparser.ConfigParser()
# 設定値の定義
config['DEFAULT'] = {
    'debug': True
}
config['web_server'] = {
    'host': '127.0.0.1',
    'port': 80
}
config['db_server'] = {
    'host': '127.0.0.1',
    'port': 3306
}
# config ファイルの書き込み
with open('files/23_config.ini', mode='w') as config_file:
    config.write(config_file)

# config ファイルの読み込み
config.read('files/23_config.ini')
print(config['web_server'])
print(config['web_server']['host'])
# 以下のように表示される
"""
<Section: web_server>
127.0.0.1
"""