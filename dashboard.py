import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# Step 1: Load the dataset
# ==============================
df = pd.read_csv("student_exam_scores.csv")

# ==============================
# Step 2: Data cleaning
# ==============================
print("Missing values in each column:")
print(df.isnull().sum())

# Remove missing rows
df = df.dropna()

# Remove duplicate rows
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")
df = df.drop_duplicates()

print("Dataset shape after cleaning:", df.shape)

# ==============================
# Step 3: Dashboard Visualization
# ==============================
plt.style.use("seaborn-v0_8")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Distribution of exam scores
sns.histplot(df["exam_score"], bins=15, kde=True, ax=axes[0,0], color="skyblue")
axes[0,0].set_title("Distribution of Exam Scores", fontsize=12)
axes[0,0].set_xlabel("Exam Score")
axes[0,0].set_ylabel("Number of Students")

# 2. Hours studied vs Exam score
sns.scatterplot(x="hours_studied", y="exam_score", data=df, ax=axes[0,1], color="blue", alpha=0.7)
axes[0,1].set_title("Hours Studied vs Exam Score", fontsize=12)
axes[0,1].set_xlabel("Hours Studied")
axes[0,1].set_ylabel("Exam Score")

# 3. Sleep hours vs Exam score
sns.scatterplot(x="sleep_hours", y="exam_score", data=df, ax=axes[1,0], color="green", alpha=0.7)
axes[1,0].set_title("Sleep Hours vs Exam Score", fontsize=12)
axes[1,0].set_xlabel("Sleep Hours")
axes[1,0].set_ylabel("Exam Score")

# 4. Attendance percent vs Exam score
sns.scatterplot(x="attendance_percent", y="exam_score", data=df, ax=axes[1,1], color="orange", alpha=0.7)
axes[1,1].set_title("Attendance Percent vs Exam Score", fontsize=12)
axes[1,1].set_xlabel("Attendance Percent")
axes[1,1].set_ylabel("Exam Score")

plt.tight_layout()
plt.show()
