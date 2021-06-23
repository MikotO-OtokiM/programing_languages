################################################################################
# yaml ファイル
import yaml

# 設定値の定義
# yaml ファイルの書き込み
with open('files/24_config.yml', mode='w') as yaml_file:
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': 3306
        }
    }, yaml_file)

# yaml ファイルの読み込み
with open('files/24_config.yml', mode='r') as yaml_file:
    data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    print(data['web_server']['host'])
    print(data['web_server']['port'])
# 以下のように表示される
"""
127.0.0.1
80
"""