import pandas as pd

df = pd.read_csv('sample_tsv.tsv', sep="\t")

# set multi Index df
df_x = df.set_index(['order_date', 'city', 'customer_id'])
for name, level in zip(df_x.index.names, df_x.index.levels):
    print(name, ':', level)
