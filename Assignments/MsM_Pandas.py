import pandas as pd

# Cricket statistics dataset
data = {
    'Player': ['Virat', 'Dhoni', 'Gayle', 'ABD', 'Raina', 'Rohit'],
    'Runs': [2500, 1800, None, 2200, 1600, 2300],
    'Innings': [80, 75, 70, None, 65, 78],
    'Fifties': [20, 15, 18, 22, None, 21],
    'Hundreds': [8, 5, 10, 7, 3, None],
    'Team': ['India', 'India', 'West Indies', 'South Africa',
             'India', 'India']
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# 1.1 Detecting missing values
print("\nMissing Values:")
print(df.isnull())

# 1.2 Counting missing values
print("\nCount of Missing Values:")
print(df.isnull().sum())

# 2. Removing rows containing missing values
df_removed = df.dropna()

print("\nAfter Removing Missing Values:")
print(df_removed)

# 3. Filling missing values
df_filled = df.copy()

df_filled['Runs'] = df_filled['Runs'].fillna(df_filled['Runs'].mean())
df_filled['Innings'] = df_filled['Innings'].fillna(df_filled['Innings'].mean())
df_filled['Fifties'] = df_filled['Fifties'].fillna(df_filled['Fifties'].mean())
df_filled['Hundreds'] = df_filled['Hundreds'].fillna(df_filled['Hundreds'].mean())

print("\nAfter Filling Missing Values:")
print(df_filled)

# 4. Grouping data
grouped = df_filled.groupby('Team')['Runs'].mean()

print("\nAverage Runs by Team:")
print(grouped)
