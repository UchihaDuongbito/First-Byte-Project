import pandas as pd

# Load the datasets from the provided files
pulsegear_data = pd.read_csv('data/pulsegear.csv')
coreboost_data = pd.read_csv('data/coreboost.csv')
chefsmeal_data = pd.read_csv('data/chefsmeal.csv')
flexfield_fitness_data = pd.read_csv('data/flexfield_fitness.csv')

# Applying mean imputation for columns with missing values
# Only apply mean imputation to numerical columns that have NaN values

# Impute missing values in PulseGear dataset for columns that have NaN values
for column in pulsegear_data.columns:
    if pulsegear_data[column].isna().sum() > 0 and pulsegear_data[column].dtype in ['float64', 'int64']:
        pulsegear_data[column] = pulsegear_data[column].fillna(pulsegear_data[column].mean())

# Impute missing values in CoreBoost dataset for columns that have NaN values
for column in coreboost_data.columns:
    if coreboost_data[column].isna().sum() > 0 and coreboost_data[column].dtype in ['float64', 'int64']:
        coreboost_data[column] = coreboost_data[column].fillna(coreboost_data[column].mean())

# Impute missing values in Chef's Meal dataset for columns that have NaN values
for column in chefsmeal_data.columns:
    if chefsmeal_data[column].isna().sum() > 0 and chefsmeal_data[column].dtype in ['float64', 'int64']:
        chefsmeal_data[column] = chefsmeal_data[column].fillna(chefsmeal_data[column].mean())

# Impute missing values in FlexField Fitness dataset for columns that have NaN values
for column in flexfield_fitness_data.columns:
    if flexfield_fitness_data[column].isna().sum() > 0 and flexfield_fitness_data[column].dtype in ['float64', 'int64']:
        flexfield_fitness_data[column] = flexfield_fitness_data[column].fillna(flexfield_fitness_data[column].mean())

# Optionally, save the imputed datasets to new files
pulsegear_data.to_csv('data/imputed_pulsegear.csv', index=False)
coreboost_data.to_csv('data/imputed_coreboost.csv', index=False)
chefsmeal_data.to_csv('data/imputed_chefsmeal.csv', index=False)
flexfield_fitness_data.to_csv('data/imputed_flexfield_fitness.csv', index=False)

# Display the first few rows of the imputed data
print("Imputed PulseGear Data:\n", pulsegear_data.head())
print("Imputed CoreBoost Data:\n", coreboost_data.head())
print("Imputed Chef's Meal Data:\n", chefsmeal_data.head())
print("Imputed FlexField Fitness Data:\n", flexfield_fitness_data.head())
