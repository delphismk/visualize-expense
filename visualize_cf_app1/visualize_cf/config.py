import os

from IPython.sphinxext.ipython_directive import OUTPUT

# 入出力パス（controllerからconfigに切り出してきた）
INPUT_DIR = "data/input_csv"
OUTPUT_DIR = "data/outputs"

CATEGORY_RULES = {
    'コンビニ' : r'(フアミリ|ファミリ|ローソン|セブン|ミニストップ|newdays)',
    '外食' : r'(マクドナルド|やよい軒|はなまる|安楽亭|スシロー)',
    'スーパー' : r'(スーパー|イオン|業務用スーパー|イトーヨーカドー)',
    '衣類' : r'(ユニクロ|ジーユー|しまむら|アパレル)',
    '交通' : r'(交通|タクシー|cycling|suica|jr|メトロ|小田急電鉄)',
    '通販' : r'(amazon|メルカリ)',
    'apple経由サブスク' : r'(apple.com/bill)'
}