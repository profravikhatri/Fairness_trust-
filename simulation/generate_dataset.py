
import numpy as np, pandas as pd
np.random.seed(42)
N=100000
participants=np.random.randint(1,500,N)
energy=np.random.lognormal(3,0.5,N)
regions=np.random.choice(["urban","rural","industrial"],N)
df=pd.DataFrame({"participant":participants,"energy":energy,"region":regions})
df.to_csv("../data/rec_transactions.csv",index=False)
print("Dataset generated:",len(df))
