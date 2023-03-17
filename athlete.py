import pandas as pd
import matplotlib.pyplot as plt
import sys

def menu():
    options = {                         # define a dictionary of choices
        '1': 'Sex',
        '2': 'Age',
        '3': 'Team',
        '4': 'Year',
        '5': 'Sport'
    }
    print("\nPlease, enter the numbers of the filters you would like to use",
          "(e.g. 234 if you want to filter by age, team and year:)")
    print("\n".join([f"\t{num}. {choice}" for num, choice in options.items()]))

    input_str = input().strip()         # get the user input string
    choices = []
    
    if len(input_str) > 5:              # if input more than 5 options
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
            if choice == 1:             # filter by sex
                sex = input("Enter F for female, M for male: ").upper()
                if sex not in ('F', 'M'):
                    raise ValueError
                temp = df[(df['Sex'] == sex)]
            
            elif choice == 2:           # filter by age
                age = int(input("Enter age in years: "))
                if age <= 0:
                    raise ValueError
                temp = df[(df['Age'] == int(age))]  
            
            elif choice == 3:           # filter by team
                team = input("Enter the name of team: ").capitalize()
                if not team.isalpha():
                    raise ValueError
                temp = df[(df['Team'] == team)]
            
            elif choice == 4:           # filter by year
                year = int(input("Enter the year: "))
                if year <= 0:
                    raise ValueError
                temp = df[(df['Year'] == int(year))]
            
            elif choice == 5:           # filter by sport
                sport = input("Enter the name of sport: ").capitalize()
                if not team.isalpha():
                    raise ValueError
                temp = df[(df['Sport'] == sport)]
            
            df = temp
    
    except ValueError:                  # if error found in filter input
        print("Invalid input found!")
        return 0, original_df
    
    return len(df), df


def plotting(records, df):
    if records <= 0:
        print("No figure generated.")
    
    else:
        plt_name = ""
        if 0 < records < 100:                 # plot scatter graph
            plt_name = "scatter.png"
            plt.scatter(df['ID'], df['Weight'])
            plt.xlabel('ID of Athletes') 
            plt.ylabel('Weight (kg)') 
            plt.title('Scatter Plot of the Weight of Selected Athletes', fontsize = '16')

        else:                           # plot histogram
            plt_name = "hist.png"
            plt.hist(df['Weight'], bins = 12)
            plt.xlabel('Weight of the Athletes (kg)') 
            plt.ylabel('Number of records') 
            plt.title('Histogram of the weight of selected Athletes', fontsize = '16')

        plt.savefig(plt_name)
        print("\n===========================================")
        print(f"{records} records")
        print(f"File {plt_name} saved")
        print("===========================================")


def main():
    original_df = pd.read_csv("athlete_events.csv") 
    records, filtered_df = filtering(original_df)
    # filtered_df.to_csv('out.csv')             # check output
    plotting(records, filtered_df)


if __name__ == "__main__":
    main()
