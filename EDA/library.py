import polars as pl


def create_custom_scanner(root_directory):
    def custom_scan_parquet(path, **kwargs):
        # ルートディレクトリと指定されたパスを結合
        full_path = root_directory + path
        return pl.scan_parquet(full_path, **kwargs)

    return custom_scan_parquet

# # 任意のルートディレクトリを設定
# my_root_directory = "/kaggle/input/child-mind-institute-detect-sleep-states/"
#
# # カスタムスキャナーを生成
# custom_scanner = create_custom_scanner(my_root_directory)
#
# # `pl.scan_parquet` にカスタムスキャナーを代入
# pl.scan_parquet = custom_scanner
#
# # `pl.scan_parquet` を呼び出すと、`my_root_directory` が適用されます
# result = pl.scan_parquet('train_series.parquet')