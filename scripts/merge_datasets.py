import pandas as pd

def merge_datasets(file1, file2, file3, output_file):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    df3 = pd.read_csv(file3)

    merged_df = pd.concat([df1, df2, df3], ignore_index=True)

    merged_df.to_csv(output_file, index=False)
    print(f"Datasets merged and saved to '{output_file}'")

merge_datasets('e:/Projects/kaim/ux-analytics-for-fintech/data/dashen_reviews_20250608_162802.csv', 'e:/Projects/kaim/ux-analytics-for-fintech/data/combanketh_reviews_20250608_162756.csv', "e:/Projects/kaim/ux-analytics-for-fintech/data/boa_reviews_20250608_162800.csv", 'e:/Projects/kaim/ux-analytics-for-fintech/data/merged_dataset.csv')
