import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets from the provided files
pulsegear_data = pd.read_csv('data/pulsegear.csv')
coreboost_data = pd.read_csv('data/coreboost.csv')
chefsmeal_data = pd.read_csv('data/chefsmeal.csv')
flexfield_fitness_data = pd.read_csv('data/flexfield_fitness.csv')

# Function to plot the distribution of columns with missing values
def plot_missing_value_distributions(data, dataset_name):
    columns_with_nan = [column for column in data.columns if data[column].isna().sum() > 0 and data[column].dtype in ['float64', 'int64']]
    
    for column in columns_with_nan:
        plt.figure(figsize=(12, 6))

        # Histogram to show the distribution
        plt.subplot(1, 2, 1)
        sns.histplot(data[column], kde=True, bins=30, color='blue')
        plt.title(f'Histogram of {column} in {dataset_name}')

        # Boxplot to show the spread and outliers
        plt.subplot(1, 2, 2)
        sns.boxplot(x=data[column], color='green')
        plt.title(f'Boxplot of {column} in {dataset_name}')

        plt.tight_layout()
        plt.show()

# Plot distributions for columns with missing values in each dataset
plot_missing_value_distributions(pulsegear_data, 'PulseGear Dataset')
plot_missing_value_distributions(coreboost_data, 'CoreBoost Dataset')
plot_missing_value_distributions(chefsmeal_data, 'Chef\'s Meal Dataset')
plot_missing_value_distributions(flexfield_fitness_data, 'FlexField Fitness Dataset')
