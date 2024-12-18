# SleepInc-Sleep-Health-Analysis

This repository contains an analysis of sleep data from SleepInc's SleepScope app. As a data science consultant, the goal is to uncover relationships between lifestyle factors (exercise, gender, occupation) and sleep quality using Python. The analysis aims to identify patterns and insights for improving sleep quality.

Dataset
The dataset includes various factors such as sleep duration, sleep quality, physical activity, stress, and demographics that may influence sleep health. The dataset is provided in a CSV file named sleep_health_data.csv and contains data for 374 individuals. It includes the following columns:

Column	Description
Person ID	An identifier for each individual.
Gender	The gender of the person (Male/Female).
Age	The age of the person in years.
Occupation	The occupation or profession of the person.
Sleep Duration (hours)	The average number of hours the person sleeps per day.
Quality of Sleep (scale: 1-10)	A subjective rating of the quality of sleep, ranging from 1 to 10.
Physical Activity Level (minutes/day)	The average number of minutes the person engages in physical activity daily.
Stress Level (scale: 1-10)	A subjective rating of the stress level experienced by the person, ranging from 1 to 10.
BMI Category	The BMI category of the person (e.g., Underweight, Normal, Overweight).
Blood Pressure (systolic/diastolic)	The average blood pressure measurement of the person, indicated as systolic/diastolic.
Heart Rate (bpm)	The average resting heart rate of the person in beats per minute.
Daily Steps	The average number of steps the person takes per day.
Sleep Disorder	The presence or absence of a sleep disorder in the person (None, Insomnia, Sleep Apnea).

Analysis Objective
The primary objective of this analysis is to investigate the relationships between:

Exercise: Daily physical activity levels and its impact on sleep quality.
Gender: Differences in sleep quality between male and female participants.
Occupation: How different occupations relate to sleep quality and health.

Methods
The following Python libraries are used for data analysis:

Pandas: For data manipulation and cleaning.
Matplotlib and Seaborn: For visualizing relationships in the data.
SciPy and Statsmodels: For statistical analysis and hypothesis testing.
Scikit-learn: For machine learning modeling and feature selection (if applicable).

Steps:
Data Preprocessing: Cleaning and transforming the dataset to make it suitable for analysis.
Exploratory Data Analysis (EDA): Visualizing the distribution of key variables (e.g., sleep duration, quality, exercise).
Correlation Analysis: Investigating correlations between sleep quality and other factors like physical activity, stress, and occupation.
Statistical Testing: Using tests such as ANOVA or t-tests to identify significant differences in sleep quality by gender, occupation, and BMI.
Modeling: (Optional) Building predictive models to forecast sleep quality based on lifestyle factors.
Requirements

The following Python libraries are required to run the analysis:

bash
Copy code
pip install pandas numpy matplotlib seaborn scipy statsmodels scikit-learn

Files
sleep_health_data.csv: The dataset provided by SleepInc.
analysis.py: The Python script containing the data analysis and modeling code.
visualizations.ipynb: An interactive Jupyter Notebook with visualizations and insights.

Insights
The analysis aims to reveal patterns such as:
The effect of physical activity on sleep quality.
Gender-based differences in sleep quality ratings.
How occupation and other demographic factors influence sleep health.
Potential lifestyle changes that could improve sleep quality.
