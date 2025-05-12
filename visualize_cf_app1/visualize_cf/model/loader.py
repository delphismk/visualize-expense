#明細データを抽出

import pandas as pd
import os
import chardet

#ご利用明細の下の行から読み込むための処理
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

#pdを使ってcsvの内容をご利用明細の下の行から読み込むための前処理
def extract_meisai_data(file_path):
    with open(file_path, 'r', encoding=detect_encoding(file_path)) as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if "【ご利用明細】" in line:
            header_index = i + 1
            data_lines = lines[header_index:]
            break
    else:
        return None

    from io import StringIO
    return pd.read_csv(StringIO(''.join(data_lines)))

#
def load_all_meisai_csv(directory_path):
    all_data = []
    for file in sorted(os.listdir(directory_path)):
        if file.endswith(".csv"):
            full_path = os.path.join(directory_path, file)
            df = extract_meisai_data(full_path)
            if df is not None:
                df["ファイル名"] = file
                all_data.append(df)
    return pd.concat(all_data, ignore_index=True)