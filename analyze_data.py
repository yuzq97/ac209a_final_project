import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/Most-Recent-Cohorts-Institution.csv", low_memory=False)
df.replace("PrivacySuppressed", np.nan, inplace=True) # privacysuppressed
missing = df.isna().sum(axis=0) / len(df) * 100
# plt.hist(missing, bins=20, color='skyblue', edgecolor='black')
# plt.title("Distribution of Missing Values per Variable")
# plt.xlabel("Percentage of Missing Values(%)")
# plt.ylabel("Number of Variables")
# plt.xticks(np.linspace(0,100,21))
# plt.grid()
# plt.tight_layout()
# plt.show()

# Calculate the percentage of missing data in each column
missing_percentage = df.isnull().mean() * 100

# Select columns where missing data is less than 5%
selected_columns = missing_percentage[missing_percentage < 5].index.tolist()

# Create a new DataFrame with these columns
new_df = df[selected_columns]
new_df.to_csv('small_institution.csv', index=False)
