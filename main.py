import open_csv
import sample
file = "fatal_shark_attacks.csv"
data = open_csv.read(file)


from_Y = input("Please enter the starting year for the information you want to view: ")
untill_Y = input("Please enter the ending year for the information you want to view: ")
data_sample = sample.countAttacksByYearRange('12','13',data) 
print(data_sample)