import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import pearsonr, spearmanr, ttest_ind, f_oneway
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data_path = "sleep_health_data.csv"
data = pd.read_csv(data_path)

# Display basic information about the dataset
print("Dataset Head:\n", data.head())
print("\nDataset Info:\n")
data.info()
print("\nMissing Values:\n", data.isnull().sum())

# Handle Missing Values (if any)
data.dropna(inplace=True)  # Dropping rows with missing values (can be modified)

# Descriptive Statistics
print("\nDescriptive Statistics:\n", data.describe())

# Convert Categorical Data to Numeric if Needed
label_encoders = {}
categorical_columns = ["Gender", "Occupation", "BMI Category", "Sleep Disorder"]
for col in categorical_columns:
    if (col in data.columns) and (data[col].dtype == 'object'):
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col].astype(str))  # Ensure consistent encoding
        label_encoders[col] = le
# Print a confirmation message
print("Categorical columns encoded:", list(label_encoders.keys()))


# -----------------------------
# Step 1: Data Visualization
# -----------------------------
sns.set(style="whitegrid")

# Distribution of Sleep Quality
plt.figure(figsize=(8, 5))
sns.histplot(data["Quality of Sleep"], kde=True, bins=10, color="blue")
plt.title("Distribution of Sleep Quality")
plt.xlabel("Quality of Sleep (scale: 1-10)")
plt.ylabel("Frequency")
plt.show()

# Boxplot: Sleep Quality by Gender
plt.figure(figsize=(8, 5))
sns.boxplot(x="Gender", y="Quality of Sleep", data=data)
plt.title("Sleep Quality by Gender")
plt.xlabel("Gender")
plt.ylabel("Quality of Sleep (scale: 1-10)")
plt.show()

# Pairplot for Numerical Variables
numerical_cols = ["Sleep Duration", "Quality of Sleep", "Physical Activity Level", "Stress Level", "Daily Steps"]
# Check if you want to differentiate by a categorical variable (e.g., "Gender") using hue
# If no categorical variable is used for color, remove the 'palette' argument
sns.pairplot(data[numerical_cols], diag_kind="kde")  # No hue, no palette argument
plt.show()


# -----------------------------
# Step 2: Group Analysis
# -----------------------------
# Average Sleep Quality by Occupation
grouped_occupation = data.groupby("Occupation")["Quality of Sleep"].mean().sort_values()
plt.figure(figsize=(10, 6))
grouped_occupation.plot(kind="bar", color="purple")
plt.title("Average Sleep Quality by Occupation")
plt.xlabel("Occupation")
plt.ylabel("Average Sleep Quality")
plt.show()

# Relationship Between Exercise and Sleep Quality
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Physical Activity Level", y="Quality of Sleep", hue="Gender", data=data)
plt.title("Physical Activity vs Sleep Quality")
plt.xlabel("Physical Activity Level (minutes/day)")
plt.ylabel("Quality of Sleep (scale: 1-10)")
plt.show()

# -----------------------------
# Step 3: Statistical Analysis
# -----------------------------
# Correlation Analysis
corr_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# Pearson Correlation: Exercise vs Sleep Quality
pearson_corr, _ = pearsonr(data["Physical Activity Level"], data["Quality of Sleep"])
print(f"Pearson Correlation (Exercise vs Sleep Quality): {pearson_corr:.2f}")

# T-Test: Sleep Quality by Gender
gender_groups = [
    data[data["Gender"] == 0]["Quality of Sleep"],  # Male
    data[data["Gender"] == 1]["Quality of Sleep"]   # Female
]
t_stat, p_value = ttest_ind(*gender_groups)
print(f"T-Test (Sleep Quality by Gender): t-stat = {t_stat:.2f}, p-value = {p_value:.3f}")

# ANOVA: Sleep Quality by Occupation
occupations = [data[data["Occupation"] == i]["Quality of Sleep"] for i in data["Occupation"].unique()]
anova_stat, anova_p = f_oneway(*occupations)
print(f"ANOVA (Sleep Quality by Occupation): F-stat = {anova_stat:.2f}, p-value = {anova_p:.3f}")

# -----------------------------
# Step 4: Regression Analysis
# -----------------------------
# Predict Sleep Quality Based on Exercise, Stress, and Gender
X = data[["Physical Activity Level", "Stress Level", "Gender"]]
y = data["Quality of Sleep"]

model = LinearRegression()
model.fit(X, y)

print("\nRegression Coefficients:")
for col, coef in zip(X.columns, model.coef_):
    print(f"{col}: {coef:.2f}")

print(f"Intercept: {model.intercept_:.2f}")