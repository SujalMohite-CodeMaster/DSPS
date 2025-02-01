import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a dataset using Pandas
df = pd.DataFrame({"values": pd.Series([*pd.Series(range(1000)).sample(500, replace=True)])})

# Create the plot
plt.figure(figsize=(10, 5))

# Matplotlib Histogram
plt.hist(df["values"], bins=30, density=True, alpha=0.6, color='b', edgecolor='black', label="Matplotlib")

# Seaborn Histogram
sns.histplot(df["values"], bins=30, stat="density", kde=True, color='r', label="Seaborn", alpha=0.6)

# Labels and title
plt.xlabel("Value")
plt.ylabel("Density")
plt.title("Normalized Histogram using Pandas, Matplotlib & Seaborn")

# Legend
plt.legend()

# Show plot
plt.show()
