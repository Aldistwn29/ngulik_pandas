import pandas as pd
import numpy as np

arr_df = np.array([[1,2,3,4],
                   [5,6,7,8],
                   ['a','b',9,10]])
df = pd.DataFrame(arr_df)
print(df.iloc[2,0:2])