import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd
import os

def _prepare_category_totals(series: pd.Series) -> pd.Series:
    """カテゴリごとの支出合計を降順＋未分類は末尾に整形"""
    if "未分類" in series.index:
        unclassified = series["未分類"]
        series = series.drop("未分類")
    else:
        unclassified = None

    series = series.sort_values(ascending=False)

    if unclassified is not None:
        series = pd.concat([series, pd.Series({"未分類": unclassified})])

    return series


def create_pie_chart(df, output_dir, title, filename, is_average=False):
    """DataFrameから円グラフを作成"""
    category_totals = df.groupby("カテゴリ")["ご利用金額(￥)"].sum()
    category_totals = _prepare_category_totals(category_totals)
    return _plot_pie_chart(category_totals, output_dir, title, filename, is_average)


def create_pie_chart_from_series(category_totals, output_dir, title, filename):
    """Series（月平均など）から円グラフを作成"""
    category_totals = _prepare_category_totals(category_totals)
    return _plot_pie_chart(category_totals, output_dir, title, filename, is_average=True)


def _plot_pie_chart(category_totals, output_dir, title, filename, is_average):
    total = category_totals.sum()
    outer_labels = list(category_totals.index)

    fig, ax = plt.subplots(figsize=(9, 9))
    wedges, texts, autotexts = ax.pie(
        category_totals,
        startangle=90,
        counterclock=False,
        labels=outer_labels,
        autopct="%1.1f%%",
        labeldistance=1.15,
        textprops={"fontsize": 9},
    )

    legend_labels = [f"{cat}: {amt:,.0f}円" for cat, amt in category_totals.items()]
    ax.legend(
        wedges,
        legend_labels,
        title="カテゴリ別支出",
        loc="center left",
        bbox_to_anchor=(1, 0.5),
        fontsize=9,
    )

    suffix = f"{'月平均' if is_average else '合計金額'}: {total:,.0f}円"
    ax.set_title(f"{title}\n{suffix}")
    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, filename))
    return fig