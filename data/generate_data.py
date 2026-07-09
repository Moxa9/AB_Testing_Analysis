import pandas as pd
import numpy as np

np.random.seed(42)

n = 10000

group = np.random.choice(['A','B'], size=n)

conversion=[]

for g in group:

    if g=='A':
        conversion.append(np.random.binomial(1,0.12))

    else:
        conversion.append(np.random.binomial(1,0.145))

df=pd.DataFrame({
    'User_ID':range(1,n+1),
    'Group':group,
    'Converted':conversion
})

df.to_csv("data/conversion_data.csv", index=False)

df.head()
