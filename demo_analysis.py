"""
Small demo: build a fake sales dataset, compute the average sale amount,
and save a bar chart of sales by record as a PNG.

Run with: python3 demo_analysis.py
"""

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "record_id": [f"S{i:02d}" for i in range(1, 11)],
    "sales": [220, 340, 180, 410, 275, 390, 150, 460, 300, 265],
}
df = pd.DataFrame(data)

average_sales = df["sales"].mean()
print(df)
print(f"\nAverage sales: {average_sales:.2f}")

fig, ax = plt.subplots(figsize=(8, 5))
bar_color = "#3B82F6"
ax.bar(df["record_id"], df["sales"], color=bar_color, width=0.6)
ax.axhline(average_sales, color="#6B7280", linestyle="--", linewidth=1)
ax.text(
    len(df) - 0.5,
    average_sales,
    f"avg = {average_sales:.0f}",
    color="#6B7280",
    va="bottom",
    ha="right",
)

ax.set_title("Fake Sales Records")
ax.set_xlabel("Record")
ax.set_ylabel("Sales ($)")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.tight_layout()
fig.savefig("demo_sales_chart.png", dpi=150)
print("Saved chart to demo_sales_chart.png")
