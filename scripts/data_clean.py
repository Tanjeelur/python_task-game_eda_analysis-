import pandas as pd
import os

# Ensure the directories exist before saving
os.makedirs('data', exist_ok=True)
os.makedirs('data/cleaned', exist_ok=True)

# Load the dataset
file_path = '../data/cricinfo_innings_data.csv'
df = pd.read_csv(file_path)

# Drop unnecessary columns and reset the index
df_cleaned = df.drop(columns=[col for col in df.columns if 'Unnamed' in col or 'Column' in col])

# Convert relevant columns to appropriate data types
# Use the correct date format for 'Start Date' (e.g., '15 Mar 1877')
df_cleaned['Start Date'] = pd.to_datetime(df_cleaned['Start Date'], format='%d %b %Y', errors='coerce')  # Ensure date is in datetime format
df_cleaned['Score'] = df_cleaned['Score'].apply(pd.to_numeric, errors='coerce')  # Convert Score to numeric values

# Handle missing values by filling them with appropriate placeholders (e.g., 'Unknown' for strings, 0 for numeric)
df_cleaned['Result'] = df_cleaned['Result'].fillna('Unknown')
df_cleaned['Target'] = df_cleaned['Target'].fillna(0)
df_cleaned['Lead'] = df_cleaned['Lead'].fillna(0)

# Remove rows with completely missing values
df_cleaned = df_cleaned.dropna(how='all')

# Check for duplicates and remove them
df_cleaned = df_cleaned.drop_duplicates()

# Save cleaned dataset
df_cleaned.to_csv('../data/cricinfo_innings_data_clean.csv', index=False)

# Display cleaned data
df_cleaned.head()
