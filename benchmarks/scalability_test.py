
import pandas as pd, time
df=pd.read_csv("../data/rec_transactions.csv")
start=time.time()
for i,row in df.iterrows():
 x=row.energy*0.8
end=time.time()
print("Processed:",len(df))
print("Time:",end-start)
print("TPS:",len(df)/(end-start))
