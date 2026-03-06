import csv
                    
#reading csv files
with open("Module 2/employees.csv", "r") as f:
    file1 = csv.reader(f)

    #next(file1) #you can skip the header  
    for row in file1:
        print(row)

data = [
    ["Tom", 26, "Delhi", 48000],
    ["Sim", 32, "Mumbai", 52000]
]

#appending to csv files
with open("Module 2/employees.csv", "a", newline="") as x:
    file2 = csv.writer(x)
    file2.writerow(["Charlie", 22, "Bangalore", 45000]) #one row
    file2.writerows(data) #multiple rows

#reading csv files as dictionary
with open("Module 2/employees.csv", "r") as y:
    file3 = csv.DictReader(y)
    for row in file3:
        print(row["Name"], row["Age"]) 

data2 = [
    {"Name": "Tom", "Age": 26, "City": "Delhi", "Salary": 48000},
    {"Name": "Sam", "Age": 32, "City": "Mumbai", "Salary": 52000}
]

#writing to csv file with dictionary
'''
with open("Module 2/employees.csv", "w", newline="") as z:
    fields = ["Name", "Age", "City", "Salary"]
    
    file4 = csv.DictWriter(z, fieldnames=fields)

    file4.writeheader()
    file4.writerows(data2)
'''
#Sometimes, CSV files may have a row as an incorrect data type
# e.g - age = "25"
# so you need to convert, age = int(row["Age"])

#let's process some data, like get the average salary 

sum = 0
count = 0
with open("Module 2/employees.csv") as idk:
    file5 = csv.DictReader(idk) #easier to read using dict instead of list

    for row in file5:
        sum += int(row["Salary"]) #incase Salary is a string
        count += 1
print(sum/count)

#above, if we use csv.reader, then we musr remember the index of the row, 
# and use that instead. e.g - row[0] , row[1]. for "Salary" it will be int(row[3])