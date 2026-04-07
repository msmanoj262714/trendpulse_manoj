import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("data/trends_analysed.csv")
os.makedirs("outputs", )

plt.plot(df["score"])
plt.savefig("outputs/score_plot.png")
plt.show()

top10 = df.nlargest(10, "score").copy()


top10["short_title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

plt.barh(top10["short_title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()  # Highest score on top

plt.savefig("outputs/chart1_top_stories.png")
plt.show()

# Count stories in each category
category_counts = df["category"].value_counts()

# Create bar chart
plt.figure(figsize=(8, 5))
plt.bar(
    category_counts.index,
    category_counts.values,
    color=["red", "blue", "green", "orange", "purple"]
)

# Add title and labels
plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")

# Save before show
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.show()  


popular = df[df["is_popular"]==True]
not_popular = df[df["is_popular"] == False]

plt.figure(figsize=(8, 5))

plt.scatter(
    popular["score"],
    popular["num_comments"],
    marker="o",
    label="Popular"
)

plt.scatter(
    not_popular["score"],
    not_popular["num_comments"],
    marker="x",
    label="Not Popular"
)

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.show()




import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/trends_analysed.csv")
os.makedirs("outputs", exist_ok=True)

# Prepare data
top10 = df.nlargest(10, "score").copy()
top10["short_title"] = top10["title"].apply(
    lambda x: x[:50] + "..." if len(x) > 50 else x
)

category_counts = df["category"].value_counts()

popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

# Create dashboard with 2x2 layout
fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# Chart 1: Top 10 stories
axes[0, 0].barh(top10["short_title"], top10["score"])
axes[0, 0].set_title("Top 10 Stories by Score")
axes[0, 0].set_xlabel("Score")
axes[0, 0].set_ylabel("Story Title")
axes[0, 0].invert_yaxis()

# Chart 2: Category counts
axes[0, 1].bar(
    category_counts.index,
    category_counts.values
)
axes[0, 1].set_title("Stories per Category")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Count")
axes[0, 1].tick_params(axis="x", rotation=30)

# Chart 3: Scatter plot
axes[1, 0].scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular"
)
axes[1, 0].scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular"
)
axes[1, 0].set_title("Score vs Comments")
axes[1, 0].set_xlabel("Score")
axes[1, 0].set_ylabel("Comments")
axes[1, 0].legend()

# Empty 4th box
axes[1, 1].axis("off")

# Overall title
fig.suptitle("TrendPulse Dashboard", fontsize=16)

# Save dashboard
plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.show()