from visualize_cf.config import CATEGORY_RULES
import re
import pandas as pd

def classify_with_regex(description):
    for category, pattern in CATEGORY_RULES.items():
        if re.search(pattern, description):
            return category
    return "未分類"

def classify_dataframe(df):
    df["カテゴリ"] = df["ご利用先など"].apply(classify_with_regex)
    return df