import os

def save_dataframe_to_csv(df, output_path):
    """
    DataFrameをCSVファイルに保存（UTF-8 with BOM）
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False, encoding="utf-8-sig")
        print(f"[✔] CSV保存完了: {output_path}")
    except Exception as e:
        print(f"[✘] CSV保存失敗: {e}")


def save_plot(fig, output_path):
    """
    matplotlibのFigureオブジェクトを画像として保存
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        fig.savefig(output_path, bbox_inches='tight')
        print(f"[✔] グラフ保存完了: {output_path}")
    except Exception as e:
        print(f"[✘] グラフ保存失敗: {e}")