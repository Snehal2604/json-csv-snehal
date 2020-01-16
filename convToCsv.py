import csv
import json

#here Attendance.json is a the already created json file
with open("Attendance.json") as file: 
    data=json.load(file)

#Attend_csv.csv is the csv file which will be already created
fname="Attend_csv.csv"

with open(fname,"w") as file:
    csv_file=csv.writer(file)
    csv_file.writerow(["Name","Age","Marks"])
    #here Result is the an array in this json file you can put your array name or leave it blank 
    for item in data["result"]:
        csv_file.writerow([item['Name'],item['Age'],item['Marks']])
