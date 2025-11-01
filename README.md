# 🤖 AI-Powered Product Insights Dashboard
**Simulated Data Project — IBM Watson Assistant**

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square) 
![Pandas](https://img.shields.io/badge/Pandas-1.6-green?style=flat-square) 
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8-orange?style=flat-square) 
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

---

## 🧠 Project Overview
This Python project analyzes **simulated IBM Watson Assistant user engagement data**, including **sessions, average duration, satisfaction scores, and feature usage over time**.

It demonstrates **data-driven product thinking, analytical reasoning, and actionable insight generation**, which are key skills for a **Product Manager Intern at IBM**, especially in teams like **IBM Data & AI** and **IBM Cloud Platform**.

By completing this project, you will understand how to:
- **Translate user interaction data into product insights**
- **Identify top-performing and underused features**
- **Visualize engagement trends over time**
- **Make data-driven recommendations to improve feature adoption and satisfaction**

---

## 🎯 Objectives
- **Analyze user sessions and feature engagement** for IBM Watson Assistant
- **Compute a composite engagement score** per feature
- **Rank feature performance and identify areas for improvement**
- **Track feature usage trends over time** using `last_used_date`
- **Recommend strategies for boosting user adoption and satisfaction**

---

## 🧩 Tools & Technologies
| **Category** | **Tool** |
|--------------|----------|
| Programming Language | Python |
| Data Manipulation | Pandas, Numpy |
| Data Visualization | Matplotlib |
| Dataset Format | Excel / CSV (Simulated Data) |
| Environment | Jupyter Notebook / VS Code / Any Python IDE |

---

## 📊 Dataset Structure
The dataset contains **50 simulated users** with the following columns:

| **Column Name** | **Description** |
|-----------------|-----------------|
| `user_id` | Unique ID for each user |
| `feature_name` | Name of the feature used (e.g., Chat Builder, Analytics Dashboard) |
| `sessions` | Number of times the user accessed the feature |
| `avg_duration_mins` | Average time spent per session (minutes) |
| `satisfaction_score` | User-reported satisfaction rating (2.5–5 scale) |
| `last_used_date` | Most recent date the user interacted with the feature |

> **Note:** The dataset is simulated for portfolio purposes and demonstrates realistic usage patterns.

---

## ⚙️ Methodology
1. **Data Loading & Cleaning:** Load dataset using `pandas` and ensure date fields are formatted correctly.  
2. **Metrics Calculation:** Compute **total sessions**, **average duration**, **satisfaction scores**, and a **composite engagement score** per feature.  
3. **Feature Ranking:** Identify top-performing features based on engagement score.  
4. **Trend Analysis:** Analyze monthly feature usage using the `last_used_date` column.  
5. **Visualization:**
   - Bar chart showing **feature engagement scores**
   - Line chart showing **monthly feature usage trends**
6. **Insights & Recommendations:** Highlight underused features and propose improvements such as **guided onboarding** or **feature visibility enhancements**.

---

## 📈 Key Insights (Example)
- **Top Feature:** Chat Builder — highest engagement and satisfaction  
- **Underused Feature:** Analytics Dashboard — low engagement indicates a need for improved onboarding or UI guidance  
- **Monthly Trends:** Revealed seasonal spikes in feature usage, helping prioritize product updates

---

## 💡 Recommendations
- Introduce a **guided onboarding wizard** for low-engagement features like Analytics Dashboard  
- Highlight underused features in the interface to increase visibility and adoption  
- Monitor engagement metrics regularly to drive continuous product improvement

---

## 📅 Project Timeline
| **Week** | **Task** |
|----------|----------|
| 1 | Data creation, cleaning, and preparation |
| 2 | Metrics calculation & Python analysis |
| 3 | Visualization & insights |
| 4 | Draft recommendations and action plan |
| 5 | Finalize report and presentation slides |

---

## 🔗 How to Run
1. ***Clone the repository:**
```bash
git clone <repository-url>

```
2. ***Install required Python packages:***
```bash
pip install pandas matplotlib openpyxl
```

3. import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("/home/nusrat/Desktop/Spreadsheet/Watson_usage_data.xlsx")


feature_usage = df.groupby("feature_name")["sessions"].sum().reset_index()


avg_duration = df.groupby("feature_name")["avg_duration_mins"].mean().reset_index()


avg_satisfaction = df.groupby("feature_name")["satisfaction_score"].mean().reset_index()


summary = (
    feature_usage
    .merge(avg_duration, on="feature_name")
    .merge(avg_satisfaction, on="feature_name")
)


summary["engagement_score"] = (
    (summary["sessions"] / summary["sessions"].max()) * 0.5 +
    (summary["avg_duration_mins"] / summary["avg_duration_mins"].max()) * 0.3 +
    (summary["satisfaction_score"] / summary["satisfaction_score"].max()) * 0.2
) * 100


top_features = summary.sort_values(by="engagement_score", ascending=False)

print("📊 Top 3 Engaging Features in IBM Watson Assistant:")
print(top_features[["feature_name", "sessions", "avg_duration_mins", "satisfaction_score", "engagement_score"]].head(3))

print("\nFeature Usage Summary:")
print(top_features)


plt.figure(figsize=(9, 5))
plt.bar(top_features["feature_name"], top_features["engagement_score"], color="skyblue")
plt.title("Feature Engagement Score (%) in IBM Watson Assistant")
plt.ylabel("Engagement Score (%)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()

---

## 🏆 Skills Demonstrated:
-Product Thinking & Customer Focus

-Data Analysis & Visualization

-Python & Excel Proficiency

-Metrics-Driven Decision Making

-Agile & Product Management Mindset

