import openCsv
import dataSelection
import dataVisualization
file = "fatal_shark_attacks.csv"
data = openCsv.read(file)

def internalOptions(data_sample, plot_title):
    chart = input(F"""{'*'*30} SELECTION CHART {'*'*30}
PRESS 1 for a bar chart 
PRESS 2 for a pie chart
PRESS 3 for bar and pie chats
->""")
    if chart == "1":
        dataVisualization.barChart(data_sample, plot_title)
    elif chart == "2":
        dataVisualization.pieChart(data_sample, plot_title)
    elif chart == "3":
        dataVisualization.barChart(data_sample, plot_title)
        dataVisualization.pieChart(data_sample, plot_title)
    else:
        raise Exception ("Invalid option")

choice = input(f"""{'*'*30} MENU {'*'*30}
PRESS 1 To see how many attacks happened in Australia in a period of time
PRESS 2 To see how many men and women were attacked by sharks in Australia since 1791 to 2022
-> """)
if choice == "1":
    from_Y = input("Please enter the starting year for the information you want to view: ")
    untill_Y = input("Please enter the ending year for the information you want to view: ")
    data_sample = dataSelection.countAttacksByYearRange(from_Y, untill_Y, data) 
    if isinstance(data_sample, dict):
        plot_title = f"Attacks happened in Australia since {from_Y} to {untill_Y}"
        internalOptions(data_sample, plot_title)

elif choice == "2":
    data_sample = dataSelection.countBySex(data) 
    plot_title = "Men and women attacked by sharks in Australia since 1791 to 2022"
    internalOptions(data_sample, plot_title)

else:
    raise Exception ("DATA NOT FOUND")

