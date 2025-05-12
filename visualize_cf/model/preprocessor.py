import pandas as pd
import unicodedata


def normalize_and_clean(df):
    # 金額列の変換（カンマ除去→float化）
    df["ご利用金額(￥)"] = (
        df["ご利用金額(￥)"]
        .astype(str)
        .str.replace(",", "")
        .astype(float)
    )

    # 日付をdatetimeに変換
    df["ご利用日"] = pd.to_datetime(df["ご利用日"], errors='coerce')

    # ご利用先を正規化（全角→半角、ひらがな→カタカナなど）
    df["ご利用先など"] = df["ご利用先など"].apply(
        lambda x: unicodedata.normalize("NFKC", str(x)).lower()
    )

    # 不要なNaN行を除外
    df = df.dropna(subset=["ご利用日", "ご利用先など", "ご利用金額(￥)"])

    return df