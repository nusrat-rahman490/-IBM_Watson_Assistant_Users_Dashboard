import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------
# Load dataset
# ------------------------------------------
df = pd.read_excel("/home/nusrat/Desktop/Spreadsheet/Watson_usage_data.xlsx")

# Sample columns you might include:
# user_id | feature_name | sessions | avg_duration_mins | satisfaction_score

# ------------------------------------------
# Calculate key product metrics
# ------------------------------------------
# Total usage per feature
feature_usage = df.groupby("feature_name")["sessions"].sum().reset_index()

# Average session duration per feature
avg_duration = df.groupby("feature_name")["avg_duration_mins"].mean().reset_index()

# Average satisfaction score
avg_satisfaction = df.groupby("feature_name")["satisfaction_score"].mean().reset_index()

# Merge all metrics into one table
summary = (
    feature_usage
    .merge(avg_duration, on="feature_name")
    .merge(avg_satisfaction, on="feature_name")
)

# ------------------------------------------
# Calculate a composite engagement score
# ------------------------------------------
summary["engagement_score"] = (
    (summary["sessions"] / summary["sessions"].max()) * 0.5 +
    (summary["avg_duration_mins"] / summary["avg_duration_mins"].max()) * 0.3 +
    (summary["satisfaction_score"] / summary["satisfaction_score"].max()) * 0.2
) * 100

# ------------------------------------------
# Sort and display results
# ------------------------------------------
top_features = summary.sort_values(by="engagement_score", ascending=False)

print("📊 Top 3 Engaging Features in IBM Watson Assistant:")
print(top_features[["feature_name", "sessions", "avg_duration_mins", "satisfaction_score", "engagement_score"]].head(3))

print("\nFeature Usage Summary:")
print(top_features)

# ------------------------------------------
# Plot engagement score per feature
# ------------------------------------------
plt.figure(figsize=(9, 5))
plt.bar(top_features["feature_name"], top_features["engagement_score"], color="skyblue")
plt.title("Feature Engagement Score (%) in IBM Watson Assistant")
plt.ylabel("Engagement Score (%)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()
