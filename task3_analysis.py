import pandas as pd
import numpy as np

# Load cleaned data
df = pd.read_csv("data/trends_clean.csv")

# Basic info
print(df.head(5))
print(df.shape)
# Basic statistics
avg = df[["score","num_comments"]].mean()
print(avg)
mean_score = np.mean(df["score"])
median_score = np.median(df["score"])
std_dev_score = np.std(df["score"])
print("__Numpy__Status__")
print(f"Mean Score: {mean_score}")
print(f"Median Score: {median_score}")
print(f"Standard Deviation of Score: {std_dev_score}")
highest_score = np.max(df["score"])
lowest_score = np.min(df["score"])
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
# Category distribution
unique_categories , counts = np.unique(df['category'], return_counts = True)
top_category = unique_categories[np.argmax(counts)]
print(f"Top category: {top_category} with {np.max(counts)} stories")
comments = df["num_comments"].to_numpy()
titles = df["title"].to_numpy()
max_comments_index = np.argmax(comments)
print("Most commented story:",titles[max_comments_index], "-",comments[max_comments_index],"comments")


# Engagement analysis
df["engagement"] = df["score"]/(df["num_comments"]+1)  # Avoid division by zero
# Top  stories 
avg_score = df["score"].mean()
df["is_popular"] = df["score"] > avg_score
# Save updated DataFrame
df.to_csv("data/trends_analysed.csv", index=False)
print("Updated DataFrame saved to data/trends_analysed.csv")