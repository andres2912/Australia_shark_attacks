import openCsv
import dataSelection
import dataVisualization
file = "fatal_shark_attacks.csv"
data = openCsv.read(file)


from_Y = input("Please enter the starting year for the information you want to view: ")
untill_Y = input("Please enter the ending year for the information you want to view: ")
data_sample = dataSelection.countAttacksByYearRange('2000','2021',data) 


bar_chart = dataVisualization.barChart(data_sample)
bar_chart = dataVisualization.pieChart(data_sample)