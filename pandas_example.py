import pandas as pd
import numpy as np

# Create sample data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'James'],
    'Age': [28, 22, 35, 32, 40],
    'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney'],
    'Salary': [50000, 45000, 65000, 55000, 70000]
}

# Create a DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n" + "="*50 + "\n")

# Basic operations
print("Basic Statistics:")
print(df.describe())
print("\n" + "="*50 + "\n")

# Filtering data
print("People above 30 years old:")
print(df[df['Age'] > 30])
print("\n" + "="*50 + "\n")

# Sorting
print("DataFrame sorted by Age:")
print(df.sort_values('Age'))
print("\n" + "="*50 + "\n")

# Grouping and aggregation
print("Average salary by city:")
print(df.groupby('City')['Salary'].mean())
print("\n" + "="*50 + "\n")

# Adding a new column
df['Experience'] = [5, 2, 10, 8, 15]
print("DataFrame with new Experience column:")
print(df)
print("\n" + "="*50 + "\n")

# Handling missing values
df.loc[2, 'Salary'] = np.nan
print("DataFrame with missing value:")
print(df)
print("\n" + "="*50 + "\n")

# Fill missing values
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print("DataFrame after filling missing values:")
print(df)
print("\n" + "="*50 + "\n")

# Export to CSV
df.to_csv('employee_data.csv', index=False)
print("Data has been exported to 'employee_data.csv'")

# Reading from CSV
df_read = pd.read_csv('employee_data.csv')
print("\nData read from CSV:")
print(df_read) 