# view/summary_console.py
def print_summary(df):
    """
    DataFrameをもとに、支出サマリをコンソールに出力する
    """
    print("\n===== 支出サマリ =====")

    total = int(df["ご利用金額(￥)"].sum())
    print(f"🔹 総支出: {total:,} 円")

    by_month = (
        df.groupby(df["ご利用日"].dt.to_period("M"))["ご利用金額(￥)"]
        .sum()
        .sort_values(ascending=False)
    )
    print("\n🔸 月別支出 TOP 3:")
    print(by_month.head(3).apply(lambda x: f"{int(x):,} 円"))

    if "カテゴリ" in df.columns:
        by_category = (
            df.groupby("カテゴリ")["ご利用金額(￥)"]
            .sum()
            .sort_values(ascending=False)
        )
        print("\n🔸 カテゴリ別支出 TOP 3:")
        print(by_category.head(3).apply(lambda x: f"{int(x):,} 円"))

    print("=====================\n")