import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("athlete_events.csv")
def filtering(df):
    """
    Filters the dataframe based on user input and returns the filtered dataframe and its length.
    """
    # Define the options for filtering
    options = {
        1: 'Sex',
        2: 'Age',
        3: 'Team',
        4: 'Year',
        5: 'Sport',
    }
    # Ask user for the filter options
    print("Please enter the digits corresponding to the features you would like to filter by, separated by commas (e.g. '123' for Sex, Age, and Team):")
    print("1: Sex")
    print("2: Age")
    print("3: Team")
    print("4: Year")
    print("5: Sport")
    filter_choices = input().strip()
    # Check if the input is valid
    if not filter_choices.isdigit() or len(filter_choices) > 5 or any(int(d) > 5 for d in filter_choices):
        print("Invalid input.")
        return 0, df
    # Ask user for the filter values
    filter_values = {}
    for digit in filter_choices:
        feature = options[int(digit)]
        filter_values[feature] = input(f"Please enter the value for {feature}: ").strip()
    # Apply the filter
    mask = pd.Series(True, index=range(len(df)))
    for feature, value in filter_values.items():
        mask &= (df[feature] == value)
    filtered_df = df[mask]
    return len(filtered_df), filtered_df

def plotting(n, df):
    """
    Generates a scatter plot or histogram based on the number of rows in the dataframe.
    """
    # Print the number of rows
    print(f"Number of records: {n}")
    # Generate plot
    if n == 0:
        pass
    elif n < 100:
        plt.scatter(df['ID'], df['Weight'])
        plt.xlabel("Athlete ID")
        plt.ylabel("Weight")
        plt.savefig("scatter.png")
        plt.show()
        print("File scatter.png saved")
    else:
        plt.hist(df['Weight'], bins=12)
        plt.xlabel("Weight")
        plt.ylabel("Frequency")
        plt.savefig("hist.png")
        plt.show()
        print("File hist.png saved")

def main():
