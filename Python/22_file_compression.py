################################################################################
# ファイル圧縮展開（tarfile）
import tarfile
# tar 圧縮
# 圧縮後のtarファイル名を指定してオープン
with tarfile.open('files/22_test.tar.gz', 'w:gz') as tr:
    # 圧縮対象のフォルダを指定
    tr.add('files/22_tar_test')

# tar 展開（該当のファイルのみ展開）
with tarfile.open('files/22_test.tar.gz', 'r:gz') as tr:
    with tr.extractfile('files/22_tar_test/test_dir/tar_test.txt') as f:
        print(f.read())

# tar 展開（全体を展開）
with tarfile.open('files/22_test.tar.gz', 'r:gz') as tr:
    # 展開先パスを指定して展開
    tr.extractall(path='files/22_open_test_tar')


################################################################################
# ファイル圧縮展開（zipfile）
import zipfile
# zip 圧縮
# 圧縮後の zip ファイル名を指定して圧縮
with zipfile.ZipFile('files/22_test.zip.zip', 'w') as z:
    # 圧縮対象のファイルを指定（フォルダまでの指定だと中のファイルは圧縮されない）
    z.write('files/22_zip_test/test_dir/zip_test.txt')
"""
# 以下のように glob ライブラリを用いるとフォルダ内の全てのファイルを簡単に圧縮できる
import glob
with zipfile.ZipFile('files/22_test.zip.zip', 'w') as z:
    for f in glob.glob('files/22_zip_test/**', recursive=True):
        z.write(f)
"""

# zip 展開（該当のファイルのみ展開）
with zipfile.ZipFile('files/22_test.zip.zip', 'r') as z:
    with z.open('files/22_zip_test/test_dir/zip_test.txt') as f:
        print(f.read())

# zip 展開（全体を展開）
with zipfile.ZipFile('files/22_test.zip.zip', 'r') as z:
    # 展開先パスを指定して展開
    z.extractall(path='files/22_open_test_zip')
