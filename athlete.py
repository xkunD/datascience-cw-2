import pandas as pd
import matplotlib.pyplot as plt
import sys

data = pd.read_csv("athlete_events.csv")

def menu():
    # define a dictionary of the choices
    options = {
        '1': 'Sex',
        '2': 'Age',
        '3': 'Team',
        '4': 'Year',
        '5': 'Sport'
    }

    print("\nPlease, enter the numbers of the filters you would like to use (e.g. 234 if you want to filter by age, team and year:)")
    # print("\t1. Sex \n\t2. Age \n\t3. Team\n\t4. Year \n\t5. Sport")
    print("\n".join([f"\t{num}. {choice}" for num, choice in options.items()]))

    input_str = input().strip()
    choices = []
    if len(input_str) > 5:
        print("Too many options")
        sys.exit()
    else:
        for num in input_str:
            if num not in options:
                print(f"{num} is not a valid option.")
                sys.exit()
            else:
                choices.append(int(num))
    return choices


def filtering():
    pass

def main():
    print("choice are:", menu())

if __name__ == "__main__":
    main()
