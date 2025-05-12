from visualize_cf.model.loader import load_all_meisai_csv
from visualize_cf.model.preprocessor import normalize_and_clean
from visualize_cf.model.classifier import classify_dataframe
from visualize_cf.model.repository import save_dataframe_to_csv, save_plot

from visualize_cf.view.pie_chart import create_pie_chart, create_pie_chart_from_series
from visualize_cf.view.summary_console import print_summary

import matplotlib.pyplot as plt
import pandas as pd
import os

from visualize_cf.config import INPUT_DIR, OUTPUT_DIR
input_dir = INPUT_DIR
output_dir = OUTPUT_DIR

def run():
    print("▶ カード明細レポート作成処理を開始します")

    # --- 1. データ読み込み ---
    df = load_all_meisai_csv(input_dir)

    # --- 2. 前処理 ---
    df = normalize_and_clean(df)

    # --- 3. カテゴリ分類 ---
    df = classify_dataframe(df)

    # --- 4. 円グラフ（全体） ---
    fig1 = create_pie_chart(df, output_dir, title="支出割合（円グラフ）", filename="category_pie_chart.png")
    save_plot(fig1, os.path.join(output_dir, "category_pie_chart.png"))

    # --- 5. 円グラフ（月別） ---
    df["年月"] = pd.to_datetime(df["ご利用日"]).dt.to_period("M")
    month_output_dir = os.path.join(output_dir, "month")
    os.makedirs(month_output_dir, exist_ok=True)

    for period, group_df in df.groupby("年月"):
        period_str = str(period)
        title = f"{period_str} 支出割合（円グラフ）"
        filename = f"{period_str}.png"

        fig = create_pie_chart(group_df, month_output_dir, title=title, filename=filename)
        save_plot(fig, os.path.join(month_output_dir, filename))

    # --- 6. 月平均カテゴリ支出グラフ ---
    monthly_avg = df.pivot_table(
        index="年月", columns="カテゴリ", values="ご利用金額(￥)", aggfunc="sum", fill_value=0
    ).mean()

    fig_avg = create_pie_chart_from_series(
        monthly_avg,
        output_dir,
        title="1ヶ月あたりの平均支出（カテゴリ別）",
        filename="average_pie_chart.png"
    )
    save_plot(fig_avg, os.path.join(output_dir, "average_pie_chart.png"))

    # --- 7. CSV出力 ---
    save_dataframe_to_csv(df, os.path.join(output_dir, "classified_data.csv"))

    # --- 8. コンソール出力 ---
    print_summary(df)

    # --- 9. 後処理 ---
    plt.close('all')