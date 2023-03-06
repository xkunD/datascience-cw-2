import pandas as pd
import matplotlib.pyplot as plt
import sys

data = pd.read_csv("athlete_events.csv")

def menu():
    print("Please, enter the numbers of the filters you would like to use (e.g. 234 if you want to filter by age, team and year:)")
    print("1. Sex \n2. Age \n3. Team\n 4. Year \n5.Sport")

    selections = str(input()).strip()
    if len(selections) > 5:
        print("Too many options")
        sys.exit()
    elif not selections.isdigit():
        print("")





def filtering():
    pass