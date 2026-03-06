
import pandas as pd
df=pd.read_csv("../data/rec_transactions.csv")
R_total=50000
total_energy=df.energy.sum()
df["r_pre"]=df.energy/total_energy*R_total
df["r_ideal"]=df.r_pre*1.1
lambda_val=0.5
df["r_post"]=df.r_pre+lambda_val*(df.r_ideal-df.r_pre)
fairness=1-abs(df.r_post-df.r_ideal).mean()
print("Fairness score:",fairness)
df.to_csv("../results/fairness_results.csv",index=False)
