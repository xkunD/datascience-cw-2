import pandas as pd
import matplotlib.pyplot as plt
import sys

def menu():
    options = {                     # define a dictionary of the choices
        '1': 'Sex',
        '2': 'Age',
        '3': 'Team',
        '4': 'Year',
        '5': 'Sport'
    }
    print("\nPlease, enter the numbers of the filters you would like to use",
          "(e.g. 234 if you want to filter by age, team and year:)")
    print("\n".join([f"\t{num}. {choice}" for num, choice in options.items()]))

    input_str = input().strip()     # get the user input string
    choices = []
    
    if len(input_str) > 5:          # if input more than 5 options
        print("Too many options")
        sys.exit()
    else:
        for choice in input_str:
            if choice not in options:   # if input value not in options
                print(f"{choice} is not a valid option.")
                sys.exit()
            else:                       # if this input valid
                choices.append(int(choice)) 
    return choices


def filtering(original_df):
    df = original_df 
    choices = menu()
    try:
        for choice in choices:
            if choice == 1:
                sex = input("Enter F for female, M for male: ").upper()
                temp = df[(df['Sex'] == sex)]
            elif choice == 2:
                age = input("Enter age in years: ")
                temp = df[(df['Age'] == int(age))]
            elif choice == 3:
                team = input("Enter the name of team: ").capitalize()
                temp = df[(df['Team'] == team)]
            elif choice == 4:
                year = input("Enter the year: ")
                temp = df[(df['Year'] == int(year))]
            elif choice == 5:
                sport = input("Enter the name of sport: ").capitalize()
                temp = df[(df['Sport'] == sport)]
            df = temp
    except ValueError:          # if errors in filter function running (maybe remove it?)
        return 0, df
    return len(df), df


def plotting(n, df):
    if 0 < n < 100:             
        # plot scatter graph
        plt.scatter(df['ID'], df['Weight'])
        plt.xlabel('ID of Athletes') 
        plt.ylabel('Weight (kg)') 
        plt.title('Scatter Plot of the Weight of Selected Athletes', fontsize = '16')
        plt.savefig("scatter.png")
        print("File scatter.png saved")

    elif n >= 100:              
        # plot histogram
        plt.hist(df['Weight'], bins = 12)
        plt.xlabel('Weight of the Athletes (kg)') 
        plt.ylabel('Number of records') 
        plt.title('Histogram of the weight of selected Athletes', fontsize = '16')
        plt.savefig("hist.png")
        print("File hist.png saved")


def main():
    original_df = pd.read_csv("athlete_events.csv") 
    records, filtered_df = filtering(original_df)
    print(filtered_df)
    plotting(records, filtered_df)


if __name__ == "__main__":
    main()
