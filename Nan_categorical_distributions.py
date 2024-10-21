import pandas as pd

# Load the datasets from the provided files
pulsegear_data = pd.read_csv('data/pulsegear.csv')
coreboost_data = pd.read_csv('data/coreboost.csv')
chefsmeal_data = pd.read_csv('data/chefsmeal.csv')

# Handling missing values for categorical columns only

# Function to handle categorical variables with missing values
def handle_categorical_missing_values(data, column_name):
    missing_percentage = (data[column_name].isna().sum() / len(data)) * 100
    print(f"Column '{column_name}' has {missing_percentage:.2f}% missing values.")
    
    if missing_percentage < 10:
        # If missing percentage is low, remove rows with missing values
        data = data.dropna(subset=[column_name])
    else:
        # If missing percentage is high, replace with mode (most frequent value)
        most_frequent = data[column_name].mode()[0]
        data[column_name] = data[column_name].fillna(most_frequent)
    
    return data

# Handling missing values in CoreBoost dataset for categorical column 'Preferred Sports Drink Type'
if pulsegear_data['Type of Apparel Purchased'].isna().sum() > 0:
    pulsegear_data_data = handle_categorical_missing_values(pulsegear_data, 'Type of Apparel Purchased')

# Handling missing values in CoreBoost dataset for categorical column 'Preferred Sports Drink Type'
if coreboost_data['Preferred Sports Drink Type'].isna().sum() > 0:
    coreboost_data = handle_categorical_missing_values(coreboost_data, 'Preferred Sports Drink Type')

# Handling missing values in Chef's Meal dataset for categorical column 'Dietary Preferences'
if chefsmeal_data['Dietary Preferences'].isna().sum() > 0:
    chefsmeal_data = handle_categorical_missing_values(chefsmeal_data, 'Dietary Preferences')

# Optionally, save the cleaned datasets to new files
# pulsegear_data.to_csv('data/categorical_pulsegear.csv', index=False)
# coreboost_data.to_csv('data/categorical_coreboost.csv', index=False)
# chefsmeal_data.to_csv('data/categorical_chefsmeal.csv', index=False)
# HAVEN'T DONE THE SAVING FILES OPTION

# Display the first few rows of the cleaned data
print("Categorical CoreBoost Data:\n", pulsegear_data.head())
print("Categorical CoreBoost Data:\n", coreboost_data.head())
print("Categorical Chef's Meal Data:\n", chefsmeal_data.head())
