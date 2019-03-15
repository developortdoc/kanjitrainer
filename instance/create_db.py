import sqlite3 

DROP_KANJIS="DROP TABLE IF EXISTS kanjis"  #すでにある場合は削除しておく
CREATE_KANJIS='''CREATE TABLE kanjis
(id INTEGER PRIMARY KEY AUTOINCREMENT, 
kanji TEXT,
jsondata TEXT)'''

conn = sqlite3.connect('kanjidb.sqlite3') #作成されたデータベースファイル
c = conn.cursor() #カーソル

c.execute(DROP_KANJIS)
c.execute(CREATE_KANJIS)
conn.commit() #一括実行
conn.close()