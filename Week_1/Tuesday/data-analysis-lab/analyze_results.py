import pandas as pd
import os

df = pd.read_csv("test_data.csv")

# print(df)

print(f"Total Test: {len(df)}")
print(df.columns)
print(df.dtypes)
print(df.head)

pass_rate = (df["status"] == "pass").mean() * 100
avg_duration = df["duration_ms"].mean()
avg_duration_sec = avg_duration / 1000
slowest = df.loc[df["duration_ms"].idxmax()]
fastest = df.loc[df["duration_ms"].idxmin()]
grouped = df.groupby("module")

print(grouped.size())
print(grouped["duration_ms"].mean())

module_pass_rate = grouped["status"].apply(
    lambda x: (x == "pass").mean() * 100
)

failed_test = df[df["status"] == "fail"]
slow_test = df[df["duration_ms"] > 1500]
auth_test = df[df["module"] == "auth"]

df["duration_sec"] = df["duration_ms"] / 1000

sorted_df = df.sort_values(by="duration_ms", ascending=False)

os.makedirs("output", exist_ok=True)
sorted_df.to_csv("output/results_sorted.csv", index=False)