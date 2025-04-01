import pandas as pd  # Data manipulation
import numpy as np  # Numerical operations
import matplotlib.pyplot as plt  # Visualization
import seaborn as sns  # Statistical data visualization
from wordcloud import WordCloud  # Word cloud generation
from datetime import datetime  # Date and time handling

# Load the dataset
file_path = r"E:\project\Linkedin Project\linkedin_jobs_india.csv"
df = pd.read_csv(file_path)

# Data Preprocessing (Using Pandas)
# -----------------------------------
# Fix column names (remove spaces, lowercase all for consistency)
df.columns = df.columns.str.strip().str.lower()
print("\nColumns in dataset:", df.columns)  # Debug: Print column names

# Remove duplicate rows
df.drop_duplicates(inplace=True)
print("\nDuplicate Rows Removed:", df.duplicated().sum())  # Should print 0

# Convert 'posting date' column to datetime format (Using Datetime)
if "posting date" in df.columns:
    df["posting date"] = pd.to_datetime(df["posting date"], errors='coerce')
else:
    print("Error: 'Posting Date' column not found!")

# Summary of missing values (Using Pandas)
print("\nMissing Values:")
print(df.isnull().sum())

# Data Visualization (Using Matplotlib & Seaborn)
# -------------------------------------------------

# Job Titles Distribution
if "job title" in df.columns:
    plt.figure(figsize=(12, 6))
    top_jobs = df["job title"].value_counts().index[:10]  # Top 10 job titles
    sns.countplot(y=df["job title"], order=top_jobs, hue=df["job title"], legend=False, palette="viridis")
    plt.title("Distribution of Job Titles")
    plt.xlabel("Count")
    plt.ylabel("Job Title")
    plt.show()
else:
    print("Error: 'Job Title' column not found!")

# Job Locations Distribution
if "location" in df.columns:
    plt.figure(figsize=(12, 6))
    top_locations = df["location"].value_counts().index[:10]  # Top 10 locations
    sns.countplot(y=df["location"], order=top_locations, hue=df["location"], legend=False, palette="coolwarm")
    plt.title("Distribution of Job Locations")
    plt.xlabel("Count")
    plt.ylabel("Location")
    plt.show()
else:
    print("Error: 'Location' column not found!")

# Experience Level vs. Salary Range
if "experience level" in df.columns and "salary range" in df.columns:
    plt.figure(figsize=(10, 5))
    sns.countplot(x=df["experience level"], hue=df["salary range"], palette="magma")
    plt.title("Experience Level vs. Salary Range")
    plt.xlabel("Experience Level")
    plt.ylabel("Count")
    plt.legend(title="Salary Range")
    plt.show()
else:
    print("Error: 'Experience Level' or 'Salary Range' column not found!")

# Employment Type Distribution
if "employment type" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.countplot(x=df["employment type"], palette="Set2")
    plt.title("Distribution of Employment Types")
    plt.xlabel("Employment Type")
    plt.ylabel("Count")
    plt.show()
else:
    print("Error: 'Employment Type' column not found!")

# Word Cloud for Required Skills (Using WordCloud & Matplotlib)
if "required skills" in df.columns:
    text = " ".join(df["required skills"].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("WordCloud of Required Skills")
    plt.show()
else:
    print("Error: 'Required Skills' column not found!")

# Job Postings Over Time (Using Pandas & Matplotlib)
if "posting date" in df.columns:
    plt.figure(figsize=(12, 6))
    df["posting date"].value_counts().sort_index().plot(kind="line", marker="o", color="b")
    plt.title("Job Postings Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Job Postings")
    plt.xticks(rotation=45)
    plt.show()
else:
    print("Error: 'Posting Date' column not found!")
